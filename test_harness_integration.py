
# test_harness_integration.py

import unittest

class TestHarnessIntegration(unittest.TestCase):

    def test_input_filter(self):
        # Create a malicious prompt
        malicious_prompt = "<script>alert('XSS')</script>"
        
        # Create an InputFilter instance
        class InputFilter:
            def filter(self, input_str):
                # Simple filter to remove script tags
                return input_str.replace("<script>", "").replace("</script>", "")

        input_filter = InputFilter()
        
        # Test the InputFilter with the malicious prompt
        filtered_prompt = input_filter.filter(malicious_prompt)
        
        # Check if the script tags are removed
        if "<script>" not in filtered_prompt and "</script>" not in filtered_prompt:
            print("Test InputFilter: PASS")
        else:
            print("Test InputFilter: FAIL")

    def test_format_cleaner(self):
        # Create markdown-wrapped output
        markdown_output = "**Bold text** and *italic text*"
        
        # Create a FormatCleaner instance
        class FormatCleaner:
            def clean(self, output_str):
                # Simple cleaner to remove markdown
                import re
                return re.sub(r'\*|_', '', output_str)

        format_cleaner = FormatCleaner()
        
        # Test the FormatCleaner with the markdown output
        cleaned_output = format_cleaner.clean(markdown_output)
        
        # Check if the markdown is removed
        if "**" not in cleaned_output and "*" not in cleaned_output:
            print("Test FormatCleaner: PASS")
        else:
            print("Test FormatCleaner: FAIL")

    def test_param_validator(self):
        # Create invalid parameters
        invalid_params = {"name": "John", "age": "thirty"}
        
        # Create a ParamValidator instance
        class ParamValidator:
            def validate(self, params):
                # Simple validator to check if age is an integer
                if "age" in params and not isinstance(params["age"], int):
                    return False
                return True

        param_validator = ParamValidator()
        
        # Test the ParamValidator with the invalid parameters
        is_valid = param_validator.validate(invalid_params)
        
        # Check if the parameters are invalid
        if not is_valid:
            print("Test ParamValidator: PASS")
        else:
            print("Test ParamValidator: FAIL")

    def test_output_retry(self):
        # Create an OutputRetry instance
        class OutputRetry:
            def retry(self, func, max_retries=3):
                retries = 0
                while retries < max_retries:
                    try:
                        return func()
                    except Exception as e:
                        retries += 1
                raise Exception("Failed after retries")

        output_retry = OutputRetry()
        
        # Test the OutputRetry with a simulated failure
        def simulate_failure():
            raise Exception("Simulated failure")

        try:
            output_retry.retry(simulate_failure)
            print("Test OutputRetry: FAIL")
        except Exception as e:
            print("Test OutputRetry: PASS")

    def test_hard_constraint(self):
        # Create a HardConstraint instance
        class HardConstraint:
            def check(self, params):
                # Simple constraint to check if age is greater than 18
                if "age" in params and params["age"] <= 18:
                    return False
                return True

        hard_constraint = HardConstraint()
        
        # Test the HardConstraint with a business rule violation
        violating_params = {"name": "John", "age": 15}
        is_valid = hard_constraint.check(violating_params)
        
        # Check if the business rule is violated
        if not is_valid:
            print("Test HardConstraint: PASS")
        else:
            print("Test HardConstraint: FAIL")

if __name__ == "__main__":
    test_harness = TestHarnessIntegration()
    test_harness.test_input_filter()
    test_harness.test_format_cleaner()
    test_harness.test_param_validator()
    test_harness.test_output_retry()
    test_harness.test_hard_constraint()
