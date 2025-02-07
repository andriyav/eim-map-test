import allure


class PrintAssertions:
    @staticmethod
    def ok_print(class_txt):
        with allure.step(f"\nMetadata = {class_txt} Ok ✅\n"):
            print(f'\nMetadata = {class_txt} Ok ✅', flush=True)

    @staticmethod
    def nok_print(class_txt):
        with allure.step(f"\nMetadata = {class_txt} Failed ❌ \n"):
            print(f'\nMetadata = {class_txt} Failed ❌ \n', flush=True)

    @staticmethod
    def title_print(title, source):
        print("\n----------------------------------------------------------------------\n", flush=True)
        print(f"{title}", flush=True)
        print(f"kw_id = {source}", flush=True)


    @staticmethod
    def no_map_print(class_txt):
        with allure.step(f"Looks like the class {class_txt} is not mapped"):
            print(f"Looks like the class {class_txt} is not mapped", flush=True)