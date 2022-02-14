from fastapi import FastAPI

import models
import tasks

app = FastAPI()


@app.post("/api/v1/enqueue")
async def enqueue(message: models.Message):
    messages_dispatched_count = 0
    for medium in message.mediums:
        for recipient in message.recipients:
            tasks.app.send_task(
                name=f'send_via_{medium}',
                kwargs={
                    'recipient': recipient,
                    'message_detail': message.message_detail
                }
            )
            messages_dispatched_count += 1
    return {'messages_dispatched_count': messages_dispatched_count, 'message': message}
