# Available Actions

Parameters are specified separately. If a parameter is not required, use `null`.

---

## Send Telegram Message

action_name: `send_telegram`

Parameters:
- param1: chat_id
- param2: text

Example:
{
  "action_name": "send_telegram",
  "param1": "chat_id",
  "param2": "text"
}

---

## Spam Mentimeter

action_name: `mentimeter`

Parameters:
- param1: code
- param2: word
- param3: times

Example:
{
  "action_name": "mentimeter",
  "param1": "code",
  "param2": "word",
  "param3": "times"
}

---

# fastCMD

## View Available Commands

action_name: `fastCMD`

Parameters:
- param1: "commands"

Example:
{
  "action_name": "fastCMD",
  "param1": "commands"
}

---

## View Public Status

Check whether the bot status is public or private.

action_name: `fastCMD`

Parameters:
- param1: "status"

Example:
{
  "action_name": "fastCMD",
  "param1": "status"
}

---

## Set Status to Public

action_name: `fastCMD`

Parameters:
- param1: "make public"

Example:
{
  "action_name": "fastCMD",
  "param1": "make public"
}

---

## Set Status to Private

action_name: `fastCMD`

Parameters:
- param1: "make private"

Example:
{
  "action_name": "fastCMD",
  "param1": "make private"
}

---

## Turn Off Bot

action_name: `fastCMD`

Parameters:
- param1: "kill"

Example:
{
  "action_name": "fastCMD",
  "param1": "kill"
}