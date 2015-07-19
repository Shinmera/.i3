from i3pystatus import Status

status = Status(standalone=True)

def format_label(label, text):
    return "<span color=\"#FFDD00\">"+label+"</span> "+text

status.register("text", text="")

status.register("clock",
                format=format_label("DATE","%a %-d %b %X"),
                hints={"markup":"pango"})

status.register("network",
                interface="wlp4s0",
                format_up=format_label("NET","{v4}"),
                format_down="NET DOWN",
                color_up="#FFFFFF",
                color_down="#FF0000",
                hints={"markup":"pango"})

status.register("battery",
                format=format_label("BAT","{percentage:.2f}%{status} {remaining:%E%hh:%Mm} {consumption:.2f}W"),
                alert=True,
                alert_percentage=5,
                status={"DIS":"↓", "CHR":"↑", "FULL":"="},
                hints={"markup":"pango"})

status.register("mem",
                format=format_label("MEM","{percent_used_mem:02}%"),
                warn_percentage=75,
                alert_percentage=90,
                color="#FFFFFF",
                warn_color="#FFFF00",
                alert_color="#FF0000",
                hints={"markup":"pango"})

status.register("cpu_usage",
                format=format_label("CPU","{usage:02}%"),
                hints={"markup":"pango"})

status.run()
