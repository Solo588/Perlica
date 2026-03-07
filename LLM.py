'''
LLM to determine intent, run actions, or chat
    1. input --> output
    2. Decifer
    3. Route to action

LLM input:
    [perlica.txt]
    [action.txt]
    [user prompt]

'''


# first create action txt for diff whitelists
def actionFile(wl):
    match wl:
        case "Admin":
            return "core/adminAction.md"

        case "whiteList":
            return "core/whitelistAction.md"

def load_txt(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def LLM(prompt, wl):
    action_path = actionFile(wl)

    base_prompt = load_txt("core/perlica.md")
    actions = load_txt(action_path)
    format_rules = load_txt("core/format.md")

    final_prompt = (
        base_prompt
        + "\n\n"
        + actions
        + "\n\n"
        + format_rules
        + "\n\nUser: "
        + prompt
    )