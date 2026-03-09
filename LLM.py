'''
LLM to determine intent, run actions, or chat
    1. input --> output
    2. Decifer
    3. Route to action

LLM input:
    [perlica.md]
    [action.md]
    [format.md]
    [chat id]
    [user prompt]

LLM output:
    work for router??
'''

from ollama import chat


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


# main
def LLM(prompt, wl, cid):
    action_path = actionFile(wl)

    perlica = load_txt("core/perlica.md")
    actions = load_txt(action_path)
    format_rules = load_txt("core/format.md")

    final_prompt = (
        perlica
        + "\n\n"
        + actions
        + "\n\n"
        + format_rules
        + "\n\n"
        + f"chatid: {cid}"
        + "\n\nUserText: "
        + prompt
    )

    response = chat(
        model="qwen2.5:7b",   # change to your model name
        messages=[
            {"role": "user", "content": final_prompt}
        ]
    )

    output = response["message"]["content"]
    return output