--[[

     Powerarrow Awesome WM theme
     github.com/lcpz

--]]

local gears = require("gears")
local lain  = require("lain")
local awful = require("awful")
local wibox = require("wibox")
local dpi   = require("beautiful.xresources").apply_dpi
local logout_menu_widget = require("themes.MyTheme.logout-menu")
local fs_widget = require("themes.MyTheme.fs-widget")
local net_speed_widget = require("themes.MyTheme.net-speed")
local cpu_widget = require("themes.MyTheme.cpu-widget")
local ram_widget = require("themes.MyTheme.ram-widget")
local volume_widget = require("themes.MyTheme.volume")


local math, string, os = math, string, os
local my_table = awful.util.table or gears.table -- 4.{0,1} compatibility

local theme                                     = {}
theme.dir                                       = os.getenv("HOME") .. "/.config/awesome/themes/MyTheme"
theme.wallpaper                                 = os.getenv("HOME") ..  "/.wallpaper/wallpaper.png"
theme.font                                      = "JetBrainsMono Regular 14"
theme.taglist_font                              = "JetBrainsMono Regular 16"
theme.fg_normal                                 = "#d8dee9"
theme.fg_focus                                  = "#88c0d0"
theme.fg_urgent                                 = "#bf616a"
theme.bg_normal                                 = "#3b4252"
theme.bg_focus                                  = "#3b4252"
theme.bg_urgent                                 = "#3b4252"
theme.taglist_fg_focus                          = "#88c0d0"
theme.taglist_fg_empty                          = "#67738f"
theme.taglist_fg_occupied                       = "#5e81ac"
theme.taglist_fg_urgent                         = "#bf616a"
theme.tasklist_bg_focus                         = "#3b4252"
theme.tasklist_fg_focus                         = "#d8dee9"
theme.tasklist_fg_normal                        = "#5e81ac"
theme.border_width                              = 2
theme.border_normal                             = "#2e3440"
theme.border_focus                              = "#81a1c1"
theme.border_marked                             = "#88c0d0"
theme.titlebar_bg_focus                         = "#4c566a"
theme.titlebar_bg_normal                        = "#4c566a"
theme.titlebar_bg_focus                         = theme.bg_focus
theme.titlebar_bg_normal                        = theme.bg_normal
theme.titlebar_fg_focus                         = theme.fg_focus
theme.text                                      = "#2e3440"
theme.menu_height                               = 26
theme.menu_width                                = 260
--theme.menu_submenu_icon                         = theme.dir .. "/icons/submenu.png"
--theme.awesome_icon                              = theme.dir .. "/icons/awesome.png"
theme.taglist_squares_sel                       = theme.dir .. "/icons/square_sel.png"
theme.taglist_squares_unsel                     = theme.dir .. "/icons/square_unsel.png"
theme.layout_tile                               = theme.dir .. "/icons/tile.png"
--theme.layout_tileleft                           = theme.dir .. "/icons/tileleft.png"
--theme.layout_tilebottom                         = theme.dir .. "/icons/tilebottom.png"
--theme.layout_tiletop                            = theme.dir .. "/icons/tiletop.png"
--theme.layout_fairv                              = theme.dir .. "/icons/fairv.png"
--theme.layout_fairh                              = theme.dir .. "/icons/fairh.png"
--theme.layout_spiral                             = theme.dir .. "/icons/spiral.png"
--theme.layout_dwindle                            = theme.dir .. "/icons/dwindle.png"
theme.layout_max                                = theme.dir .. "/icons/max.png"
theme.layout_fullscreen                         = theme.dir .. "/icons/fullscreen.png"
--theme.layout_magnifier                          = theme.dir .. "/icons/magnifier.png"
theme.layout_floating                           = theme.dir .. "/icons/floating.png"
--theme.layout_max                                = theme.dir .. "/icons/max.png"
--theme.widget_ac                                 = theme.dir .. "/icons/ac.png"
--theme.widget_battery                            = theme.dir .. "/icons/battery.png"
--theme.widget_battery_low                        = theme.dir .. "/icons/battery_low.png"
--theme.widget_battery_empty                      = theme.dir .. "/icons/battery_empty.png"
--theme.widget_mem                                = theme.dir .. "/icons/mem.png"
--theme.widget_cpu                                = theme.dir .. "/icons/cpu.png"
--theme.widget_temp                               = theme.dir .. "/icons/temp.png"
--theme.widget_net                                = theme.dir .. "/icons/net.png"
--theme.widget_hdd                                = theme.dir .. "/icons/hdd.png"
--theme.widget_music                              = theme.dir .. "/icons/note.png"
--theme.widget_music_on                           = theme.dir .. "/icons/note.png"
--theme.widget_music_pause                        = theme.dir .. "/icons/pause.png"
--theme.widget_music_stop                         = theme.dir .. "/icons/stop.png"
--theme.widget_vol                                = theme.dir .. "/icons/vol.png"
--theme.widget_vol_low                            = theme.dir .. "/icons/vol_low.png"
--theme.widget_vol_no                             = theme.dir .. "/icons/vol_no.png"
--theme.widget_vol_mute                           = theme.dir .. "/icons/vol_mute.png"
--theme.widget_mail                               = theme.dir .. "/icons/mail.png"
--theme.widget_calander                           = theme.dir .. "/icons/calander.png"
theme.widget_cal                                = theme.dir .. "/icons/cal.svg"
--theme.widget_mail_on                            = theme.dir .. "/icons/mail_on.png"
theme.widget_task                               = theme.dir .. "/icons/task.png"
--theme.widget_scissors                           = theme.dir .. "/icons/scissors.png"
--theme.widget_weather                            = theme.dir .. "/icons/dish.png"
theme.tasklist_plain_task_name                  = true
theme.tasklist_disable_icon                     = true
theme.useless_gap                               = 0
theme.titlebar_close_button_focus               = theme.dir .. "/icons/titlebar/close_focus.png"
theme.titlebar_close_button_normal              = theme.dir .. "/icons/titlebar/close_normal.png"
theme.titlebar_ontop_button_focus_active        = theme.dir .. "/icons/titlebar/ontop_focus_active.png"
theme.titlebar_ontop_button_normal_active       = theme.dir .. "/icons/titlebar/ontop_normal_active.png"
theme.titlebar_ontop_button_focus_inactive      = theme.dir .. "/icons/titlebar/ontop_focus_inactive.png"
theme.titlebar_ontop_button_normal_inactive     = theme.dir .. "/icons/titlebar/ontop_normal_inactive.png"
theme.titlebar_sticky_button_focus_active       = theme.dir .. "/icons/titlebar/sticky_focus_active.png"
theme.titlebar_sticky_button_normal_active      = theme.dir .. "/icons/titlebar/sticky_normal_active.png"
theme.titlebar_sticky_button_focus_inactive     = theme.dir .. "/icons/titlebar/sticky_focus_inactive.png"
theme.titlebar_sticky_button_normal_inactive    = theme.dir .. "/icons/titlebar/sticky_normal_inactive.png"
theme.titlebar_floating_button_focus_active     = theme.dir .. "/icons/titlebar/floating_focus_active.png"
theme.titlebar_floating_button_normal_active    = theme.dir .. "/icons/titlebar/floating_normal_active.png"
theme.titlebar_floating_button_focus_inactive   = theme.dir .. "/icons/titlebar/floating_focus_inactive.png"
theme.titlebar_floating_button_normal_inactive  = theme.dir .. "/icons/titlebar/floating_normal_inactive.png"
theme.titlebar_maximized_button_focus_active    = theme.dir .. "/icons/titlebar/maximized_focus_active.png"
theme.titlebar_maximized_button_normal_active   = theme.dir .. "/icons/titlebar/maximized_normal_active.png"
theme.titlebar_maximized_button_focus_inactive  = theme.dir .. "/icons/titlebar/maximized_focus_inactive.png"
theme.titlebar_maximized_button_normal_inactive = theme.dir .. "/icons/titlebar/maximized_normal_inactive.png"

local markup = lain.util.markup
local separators = lain.util.separators


-- Textclock
local clockicon = wibox.widget.imagebox(theme.widget_clock)
local clock = awful.widget.watch(
    "date +'%a %d %b %R'", 60,
    function(widget, stdout)
        widget:set_markup(" " .. markup.fontfg(theme.font,"#d8dee9", stdout))
    end
)

-- Calendar
local calicon = wibox.widget.imagebox(theme.widget_cal)
theme.cal = lain.widget.cal({
    attach_to = { clock },
    notification_preset = {
        font = "JetBrainsMono Regular 12",
        fg   = theme.fg_normal,
        bg   = theme.bg_normal
    }
})

--[[
-- ALSA volume
theme.volume = lain.widget.alsabar({
    --togglechannel = "IEC958,3",
    notification_preset = { font = "#a3be8c", fg = "#a3be8c" },
})
--]]


-- MEM
local memicon = wibox.widget.imagebox(theme.widget_mem)
local mem = lain.widget.mem({
    settings = function()
        widget:set_markup(markup.fontfg(theme.font,"#d8dee9", mem_now.used .. "MB "))
    end
})

--[[
-- CPU
local cpuicon = wibox.widget.imagebox(theme.widget_cpu)
local cpu = lain.widget.cpu({
    settings = function()
        widget:set_markup(markup.fontfg(theme.font,"#81a1c1", cpu_now.usage .. "% "))
    end
})
]]
--]]

--[[
-- Coretemp (lain, average)
local tempicon = wibox.widget.imagebox(theme.widget_temp)
local temp = lain.widget.temp({
    settings = function()
        widget:set_markup(markup.fontfg(theme.font, "#d08770", coretemp_now .. "°C "))
    end
})
]]
--]]


--[[
-- ALSA volume
local volicon = wibox.widget.imagebox(theme.widget_vol)
theme.volume = lain.widget.alsa({
    settings = function()
        if volume_now.status == "off" then
            volicon:set_image(theme.widget_vol_mute)
        elseif tonumber(volume_now.level) == 0 then
            volicon:set_image(theme.widget_vol_no)
        elseif tonumber(volume_now.level) <= 50 then
            volicon:set_image(theme.widget_vol_low)
        else
            volicon:set_image(theme.widget_vol)
        end

        widget:set_markup(markup.fontfg(theme.font, "#a3be8c", volume_now.level .. "% "))
    end
})
--]]


--[[
-- Net
local neticon = wibox.widget.imagebox(theme.widget_net)
local net = lain.widget.net({
    settings = function()
        widget:set_markup(markup.fontfg(theme.font, "#b48ead",  net_now.received .. " ↓↑ " .. net_now.sent .. " "))
    end
})
--]]
local pacupdates = awful.widget.watch('bash -c "checkupdates | wc -l"', 600, function(widget, stdout)
    widget:set_markup(markup.fontfg("Font Awesome 5 Free Solid", "#d8dee9", "   " .. stdout .. " "))
end)


-- Separators
tbox_separator = wibox.widget.textbox("|")


function theme.at_screen_connect(s)
    -- Quake application
   -- s.quake = lain.util.quake({ app = awful.util.terminal })
   s.quake = lain.util.quake({ app = "alacritty", height = 0.50, argname = "--name %s" })



    -- If wallpaper is a function, call it with the screen
    local wallpaper = theme.wallpaper
    if type(wallpaper) == "function" then
        wallpaper = wallpaper(s)
    end
    gears.wallpaper.maximized(wallpaper, s, true)

    -- All tags open with layout 1
    awful.tag(awful.util.tagnames, s, awful.layout.layouts[1])

    -- Create a promptbox for each screen
    s.mypromptbox = awful.widget.prompt()
    -- Create an imagebox widget which will contains an icon indicating which layout we're using.
    -- We need one layoutbox per screen.
    s.mylayoutbox = awful.widget.layoutbox(s)
    s.mylayoutbox:buttons(my_table.join(
                           awful.button({ }, 1, function () awful.layout.inc( 1) end),
                           awful.button({ }, 3, function () awful.layout.inc(-1) end),
                           awful.button({ }, 4, function () awful.layout.inc( 1) end),
                           awful.button({ }, 5, function () awful.layout.inc(-1) end)))
    -- Create a taglist widget
    s.mytaglist = awful.widget.taglist(s, awful.widget.taglist.filter.all, awful.util.taglist_buttons)

    -- Create a tasklist widget
    s.mytasklist = awful.widget.tasklist(s, awful.widget.tasklist.filter.currenttags, awful.util.tasklist_buttons)

    -- Create the wibox
    s.mywibox = awful.wibar({ position = "top", screen = s, height = 26, bg = theme.bg_normal, fg = theme.fg_normal })

    -- Add widgets to the wibox
    s.mywibox:setup {
        layout = wibox.layout.align.horizontal,
        { -- Left widgets
            layout = wibox.layout.fixed.horizontal,
            s.mytaglist,
            --spr,
            s.mypromptbox,
            spr,
        },
        s.mytasklist, -- Middle widget
        { -- Right widgets
            layout = wibox.layout.fixed.horizontal,
            wibox.widget.systray(),

            wibox.widget{tbox_separator, layout = wibox.layout.align.horizontal },
            --wibox.widget { volicon, theme.volume.widget, layout = wibox.layout.align.horizontal },
            volume_widget(),

            wibox.widget{tbox_separator, layout = wibox.layout.align.horizontal },
            wibox.widget { ram_widget{color_used="#bf616a", color_free="#a3be8c", color_buff="#ebcb8b",} , mem.widget, layout = wibox.layout.align.horizontal },

            wibox.widget{tbox_separator, layout = wibox.layout.align.horizontal },
            --wibox.widget { cpuicon, cpu.widget, layout = wibox.layout.align.horizontal },
            cpu_widget({
                    width = 70,
                    step_width = 2,
                    step_spacing = 0,
                    color = '#a3be8c'
            }),

            wibox.widget{tbox_separator, layout = wibox.layout.align.horizontal },
            wibox.widget { pacupdates, layout = wibox.layout.align.horizontal },
            --wibox.widget{tbox_separator, layout = wibox.layout.align.horizontal },
            --wibox.widget { tempicon, temp.widget, layout = wibox.layout.align.horizontal },

            wibox.widget{tbox_separator, layout = wibox.layout.align.horizontal },
            wibox.widget { net_speed_widget(), layout = wibox.layout.align.horizontal },

            wibox.widget{tbox_separator, layout = wibox.layout.align.horizontal },
            wibox.widget { calicon, clock, layout = wibox.layout.align.horizontal },

            wibox.widget{tbox_separator, layout = wibox.layout.align.horizontal },
            fs_widget(),

            wibox.widget{tbox_separator, layout = wibox.layout.align.horizontal },
            s.mylayoutbox,

            wibox.widget{tbox_separator, layout = wibox.layout.align.horizontal },
            logout_menu_widget(),

        },
    }
end

return theme
