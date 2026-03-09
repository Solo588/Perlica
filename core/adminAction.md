# Available Actions

Parameters are specified separately. If a parameter is not required, use `null`.

---
If **requirements** aren't met, **clarifications** set to **true**

## Action: send_telegram
**requirements:** reciever chat_id, text
- `param1`: `chat_id`
- `param2`: `text`
- `param3`: `null`

## Action: mentimeter
**requirements:** code, word, times
- `param1`: {code}
- `param2`: {word}
- `param3`: {times}

## Action: fastCMD commands
- `param1`: `command`
- `param2`: `null`
- `param3`: `null`

Allowed commands for `fastCMD param1`:
- `commands`
- `status`
- `make public`
- `make private`
- `kill`