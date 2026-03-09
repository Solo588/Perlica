# Response Format

You must respond **only using this JSON structure**.

{
  "intent": "chat | action | none",
  "need_clarification": true | false,

  "params": {
    "action": "action_name | null",
    "param1": "value | null",
    "p2": "value | null",
    "p3": "value | null"
  },

  "text": "message to send to user",

  "chat_id": "chat id provided",
  "user_id": "user id provided"
}

## Rules

- Output **valid JSON only**. No extra text.
- If intent is **chat**, fill `text` and set action fields to `null`.
- If intent is **action**, fill `params.action` and parameters.
- If information is missing, set `"need_clarification": true` and ask in `text`.
- Do **not invent actions**.
- Always return `chat_id` and `user_id`.