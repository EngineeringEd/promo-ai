from promo_ai.promo_json import PromoUnderstander

from llama_index.core.llms import ChatMessage, MessageRole
from promo_ai.prompts import complex_test


def main():
    """
    Toy entrypoint for the understander. Used in absence of tests in the repo to check
    it can produce output based on a complex prompt.
    """

    p = PromoUnderstander()
    second = ChatMessage(role=MessageRole.USER, content=complex_test)
    res = p.send_message(content=second.content)

    print(res)


if __name__ == "__main__":
    main()
    