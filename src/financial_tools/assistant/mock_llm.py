class MockLLM:


    def generate(self, prompt):

        return (
            "Generated answer based on financial context:\n\n"
            + prompt[:300]
        )