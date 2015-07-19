from i3pystatus import Status

status = Status(standalone=True)

status.register("text", text="")

status.register("clock", format="%a %-d %b %X")

status.register("network",
                interface="wlp4s0",
                format_up="NET {v4}",
                format_down="NET DOWN",
                color_up="#FFFFFF",
                color_down="#FF0000")

status.register("battery",
                format="BAT {percentage:.2f}%{status} {remaining:%E%hh:%Mm} {consumption:.2f}W",
                alert=True,
                alert_percentage=5,
                status={
                    "DIS": "↓",
                    "CHR": "↑",
                    "FULL": "=",
                })

status.register("mem",
                format="MEM {percent_used_mem:02}%",
                warn_percentage=75,
                alert_percentage=90,
                color="#FFFFFF",
                warn_color="#FFFF00",
                alert_color="#FF0000")

status.register("cpu_usage",
                format="CPU {usage:02}%")

status.run()
