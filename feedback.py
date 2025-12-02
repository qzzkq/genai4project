from openai import OpenAI
from dotenv import load_dotenv
import json
import os

from feedback_helper import generate_prompt

load_dotenv()
openAI_client = OpenAI(
  api_key=os.getenv("OPENAI_API_KEY")
)

personas_path = "categorized_personas.json"
persona_types = [
    "low_income_pragmatic_youth",
    "price_sensitive_students",
    "digital_native_trend_followers",
    "tech_focused_professionals",
    "high_income_quality_seekers",
    "family_oriented_adults",
    "health_wellness_enthusiasts",
    "eco_conscious_citizens",
    "luxury_lifestyle_buyers",
    "active_travelers_explorers",
    "home_improvers_diy",
    "financially_conservative_adults",
    "senior_value_seekers",
    "traditional_offline_oriented_consumers",
    "culturally_engaged_creatives"
]


class AdTest:
    def __init__(self, model="gpt-4o-mini-2024-07-18"):
        self.model = model


    def _get_result(self, message) -> str:
        completion = openAI_client.chat.completions.create(
            model=self.model,
            messages=[{"role": "system", "content": message}]
        )
        return completion.choices[0].message.content

    
    def run_test(self, ad: str, types: list[str]) -> tuple[str, str]:
        result = []

        prompt = generate_prompt(ad, types)
        print("\n\n\nel proompt type:\n\n\n", type(prompt))
        prompt_result = self._get_result(prompt)

        result.append(ad)
        result.append(prompt_result)

        return result



if __name__ == "__main__":
    tester = AdTest()

    test_ad = """iPhone 17 — твой следующий уровень технологий!
Ощути невероятную скорость, улучшенную камеру и долгий срок работы батареи.
💥 Скидка 10% только сегодня!"""

    result = tester.run_test(test_ad, ["low_income_pragmatic_youth"])

    print(result[0])
    print(result[1])