from libqtile.dgroups import simple_key_binder
import os
import re
import socket
import subprocess

from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen, Rule
from libqtile.lazy import lazy
from libqtile.widget import Spacer

mod = "mod4"

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod, "control"], "n", lazy.layout.normalize(),
        desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "s",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "comma", lazy.to_screen(0)),
    Key([mod], "period", lazy.to_screen(1)),
    Key([mod, "shift"], "f", lazy.window.toggle_floating(), desc="toggle floating"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="toggle fullscreen"),
    Key([mod], "Return", lazy.spawn("alacritty -e zsh"), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.restart(), desc="Reload the config"),
    Key([mod, "shift"], "x", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "n", lazy.spawn("geany")),
    Key([mod], "v", lazy.spawn("virt-manager")),
    Key([mod, "shift"], "v", lazy.spawn("barrier")),
    Key([mod], "Escape", lazy.spawn("xkill")),
    Key([mod], "Return", lazy.spawn("alacritty -e zsh")),
    Key([mod], "a", lazy.spawn("aseprite")),
    Key([mod], "b", lazy.spawn("firefox")),
    Key([mod], "u", lazy.spawn("unityhub")),
    Key([mod], "m", lazy.spawn("blender")),
    Key([mod], "g", lazy.spawn("godot")),
    Key([mod], "e", lazy.spawn("emacsclient -c")),
    Key([mod], "s", lazy.spawn("steam")),
    Key([mod], "o", lazy.spawn("libreoffice")),
    Key([mod], "c", lazy.spawn("code")),
    Key([mod], "t", lazy.spawn("torbrowser-launcher")),
    Key([mod], "p", lazy.spawn("keepassxc")),
    # SUPER + SHIFT KEYS
    Key([mod, "shift"], "Return", lazy.spawn("pcmanfm")),
    Key([mod], "d", lazy.spawn('dmenu_run -h 26 -i -p "Run: "')),
    # MULTIMEDIA KEYS
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 1%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 1%+")),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),
    Key([], "XF86AudioPlay", lazy.spawn("mpc toggle")),
    Key([], "XF86AudioNext", lazy.spawn("mpc next")),
    Key([], "XF86AudioPrev", lazy.spawn("mpc prev")),
    Key([], "XF86AudioStop", lazy.spawn("mpc stop")),
]

# groups = [Group(i) for i in "1234567"]
#
# for i in groups:
#    keys.extend(
#        [
#            # mod1 + letter of group = switch to group
#            Key(
#                [mod],
#                i.name,
#                lazy.group[i.name].toscreen(),
#                desc="Switch to group {}".format(i.name),
#            ),
#            # mod1 + shift + letter of group = switch to & move focused window to group
#            Key(
#                [mod, "shift"],
#                i.name,
#                lazy.window.togroup(i.name, switch_group=True),
#                desc="Switch to & move focused window to group {}".format(i.name),
#            ),
#            # Or, use below if you prefer not to switch to that group.
#            # # mod1 + shift + letter of group = move focused window to group
#            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
#            #     desc="move focused window to group {}".format(i.name)),
#        ]
#    )

groups = [
    Group("1:", matches=[Match(wm_class="godot"), Match(wm_class="Godot")]),
    Group(
        "2:",
        matches=[
            Match(wm_class="steam"),
            Match(wm_class="virt-manager"),
            Match(wm_class="barrier"),
        ],
    ),
    Group("3:", matches=[Match(wm_class="code"), Match(wm_class="emacs")]),
    Group(
        "4:",
        matches=[
            Match(wm_class="aseprite"),
            Match(wm_class="gimp"),
            Match(wm_class="krita"),
            Match(wm_class="Blender"),
        ],
    ),
    Group("5:", matches=[Match(wm_class="firefox"),
          Match(wm_class="chromium")]),
    Group("6:", matches=[Match(wm_class="geany"), Match(wm_class="pcmanfm")]),
    Group("7:", matches=[Match(wm_class="Alacritty")]),
]

# Allow MODKEY+[0 through 9] to bind to groups, see https://docs.qtile.org/en/stable/manual/config/groups.html
# MOD4 + index Number : Switch to Group[index]
# MOD4 + shift + index Number : Send active window to another Group

dgroups_key_binder = simple_key_binder("mod4")

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())


def init_layout_theme():
    return {
        "margin": 4,
        "border_width": 2,
        "border_focus": "#a3be8c",
        "border_normal": "#4c566a",
    }


layout_theme = init_layout_theme()

layouts = [
    layout.Max(**layout_theme),
    layout.Columns(**layout_theme),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]


def init_colors():
    return [
        ["#d8dee9", "#d8dee9"],  # color 0   white
        ["#3b4252", "#3b4252"],  # color 1   black
        ["#382E63", "#382E63"],  # color 2   Dark Purple
        ["#d08770", "#d08770"],  # color 3   orange
        ["#b48ead", "#b48ead"],  # color 4   pink
        ["#656f7d", "#656f7d"],  # color 5   Dark Grey
        ["#bf616a", "#bf616a"],  # color 6   red
        ["#ebcb8b", "#ebcb8b"],  # color 7   yellow
        ["#e5e9f0", "#e5e9f0"],  # color 8   light grey
        ["#88c0d0", "#88c0d0"],  # color 9   light blue
        ["#81a1c1", "#81a1c1"],  # color 10  blue
        ["#a3be8c", "#a3be8c"],  # color 11  green
    ]


colors = init_colors()


# WIDGETS FOR THE BAR


def init_widgets_defaults():
    return dict(
        font="FontAwesome5Free-Solid", fontsize=16, padding=2, background=colors[1]
    )


widget_defaults = init_widgets_defaults()

extension_defaults = widget_defaults.copy()


def init_widgets_list():
    widgets_list = [
        widget.GroupBox(
            font="FontAwesome",
            fontsize=16,
            margin_y=1,
            margin_x=0,
            padding_y=6,
            padding_x=5,
            borderwidth=3,
            disable_drag=True,
            active=colors[10],
            inactive=colors[5],
            rounded=False,
            highlight_color=colors[1],
            highlight_method="line",
            this_current_screen_border=colors[11],
            this_screen_border=colors[6],
            other_current_screen_border=colors[11],
            other_screen_border=colors[6],
            foreground=colors[2],
            background=colors[1],
        ),
        widget.Sep(linewidth=1, padding=10,
                   foreground=colors[9], background=colors[1]),
        widget.CurrentLayout(
            font="JetBrainsMono", foreground=colors[8], background=colors[1]
        ),
        widget.Sep(linewidth=1, padding=10,
                   foreground=colors[9], background=colors[1]),
        widget.WindowName(
            font="JetBrainsMono",
            fontsize=14,
            foreground=colors[8],
            background=colors[1],
        ),
        widget.Systray(background=colors[1], icon_size=20, padding=4),
        widget.Sep(linewidth=1, padding=10,
                   foreground=colors[3], background=colors[1]),
        widget.TextBox(
            font="Font Awesome 5 Free Solid",
            text="  ",
            foreground=colors[3],
            background=colors[1],
            padding=0,
            fontsize=16,
        ),
        widget.Volume(
            background=colors[1],
            foreground=colors[8],
            padding=3,
            update_interval=0.2,
            font="JetBrainsMono",
        ),
        widget.Sep(linewidth=1, padding=10,
                   foreground=colors[6], background=colors[1]),
        widget.TextBox(
            font="Font Awesome 5 Free Solid",
            text="  ",
            foreground=colors[6],
            background=colors[1],
            padding=0,
            fontsize=16,
        ),
        widget.CPU(
            foreground=colors[8],
            background=colors[1],
            format="{freq_current}GHz {load_percent}%",
            core="all",
            type="box",
        ),
        widget.Sep(linewidth=1, padding=10,
                   foreground=colors[4], background=colors[1]),
        widget.TextBox(
            font="Font Awesome 5 Free Solid",
            text="  ",
            foreground=colors[4],
            background=colors[1],
            padding=0,
            fontsize=16,
        ),
        widget.Memory(
            font="JetBrainsMono",
            measure_mem="G",
            format="{MemUsed: .2f}{mm}/{MemTotal: .0f}{mm}",
            update_interval=1,
            fontsize=14,
            foreground=colors[8],
            background=colors[1],
        ),
        widget.Sep(linewidth=1, padding=10,
                   foreground=colors[7], background=colors[1]),
        widget.TextBox(
            font="Font Awesome 5 Free Solid",
            text="  ",
            foreground=colors[7],
            background=colors[1],
            padding=0,
            fontsize=16,
        ),
        widget.CheckUpdates(
            foreground=colors[8],
            background=colors[1],
            colour_have_updates=colors[6],
            colour_no_updates=colors[8],
            padding=3,
            distro="Arch_checkupdates",
            font="JetBrainsMono",
            no_update_string="0",
            update_interval=200,
        ),
        widget.Sep(
            linewidth=1, padding=10, foreground=colors[10], background=colors[1]
        ),
        widget.TextBox(
            font="Font Awesome 5 Free Solid",
            text="  ",
            foreground=colors[10],
            background=colors[1],
            padding=0,
            fontsize=16,
        ),
        widget.DF(
            background=colors[1],
            foreground=colors[8],
            padding=3,
            font="JetBrainsMono",
            partition="/",
            format="{uf}{m}",
            visible_on_warn=False,
            warn_space=10,
            warm_color="ff0000",
            update_interval=60,
        ),
        widget.Sep(
            linewidth=1, padding=10, foreground=colors[11], background=colors[1]
        ),
        widget.TextBox(
            font="FontAwesome",
            text="  ",
            foreground=colors[11],
            background=colors[1],
            padding=0,
            fontsize=16,
        ),
        widget.Clock(
            foreground=colors[8],
            background=colors[1],
            fontsize=14,
            format="%Y-%m-%d %H:%M",
            font="JetBrainsMono",
        ),
    ]
    return widgets_list


widgets_list = init_widgets_list()


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1


def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2


widgets_screen1 = init_widgets_screen1()
widgets_screen2 = init_widgets_screen2()


def init_screens():
    return [
        Screen(top=bar.Bar(widgets=init_widgets_screen1(), size=26)),
        Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=26)),
    ]


screens = init_screens()

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

# dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="confirm"),
        Match(wm_class="dialog"),
        Match(wm_class="download"),
        Match(wm_class="error"),
        Match(wm_class="file_progress"),
        Match(wm_class="notification"),
        Match(wm_class="splash"),
        Match(wm_class="toolbar"),
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/scripts/autostart.sh"])


@hook.subscribe.startup
def start_always():
    # Set the cursor to something sane in X
    subprocess.Popen(["xsetroot", "-cursor_name", "left_ptr"])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
