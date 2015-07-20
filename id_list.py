import json
import subprocess

def run(cmd):
    output = []
    if (cmd):
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in p.stdout.readlines():
            output.append(line.rstrip())
    return output

def parse_i3_output(output_list):
    output_string = ""
    for line in output_list:
        output_string += line
    return json.loads(output_string)

def i3_msg(t, m=""):
    return parse_i3_output(run("i3-msg -t "+t+" "+m))

def equal(a,b):
    return a == b

def check(d, k, v, cmp=equal):
    return (d.has_key(k) and cmp(d[k], v))

def traverse_nodes(d, func):
    if(check(d, "nodes", list, isinstance)):
        for node in d["nodes"]:
            result = func(node)
            if (result != None):
                return result
    return None

def find_focused_node(d):
    if(check(d, "focused", True)):
        return d

    return traverse_nodes(d, find_focused_node)

def find_active_workspace(d):
    if(check(d, "type", "workspace")):
        return d if find_focused_node(d) else None
    else:
        return traverse_nodes(d, find_active_workspace)

def is_usable_window(d):
    return (not check(d, "layout", "dockarea")
            and not check(d, "name", "i3bar for output", lambda x,y: x!=None and x.startswith(y))
            and not check(d, "window", None))

def find_usable_windows(workspace):
    windows=[]
    def maybe_add_window(node):
        if (is_usable_window(node)):
            windows.append(node)
        return traverse_nodes(node, maybe_add_window)
    traverse_nodes(workspace, maybe_add_window)

    return windows

def main():
    windows = find_usable_windows(find_active_workspace(i3_msg("get_tree")))

    index = 0
    for w in windows:
        if (check(w, "focused", True)): break
        index += 1

    index += 1
    if (index >= len(windows)):
        index = 0
        
    print windows[index]["window"]

main()
