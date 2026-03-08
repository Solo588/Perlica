# Available Actions

Return the action in `parameters.action`.

Return inputs in:
- `param1`
- `param2`
- `param3`

If not needed, return `null`.

---

## Action: send_telegram
- `param1`: `chat_id`
- `param2`: `text`
- `param3`: `null`

## Action: mentimeter
- `param1`: `code`
- `param2`: `word`
- `param3`: `times`

## Action: fastCMD
- `param1`: command
- `param2`: `null`
- `param3`: `null`

Allowed commands for `fastCMD param1`:
- `commands`
- `status`
- `make public`
- `make private`
- `kill`