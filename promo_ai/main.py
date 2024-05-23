from promo_ai.promo_json import PromoUnderstander

from llama_index.core.llms import ChatMessage, MessageRole
from promo_ai.prompts import complex_test


def main():
    p = PromoUnderstander()
    second = ChatMessage(role=MessageRole.USER, content=complex_test)
    res = p.send_message(second)

    print(res)

