import re


def open_file(file_path: str) -> list[str]:
    try:
        with open(file_path) as file:
            return file.read().strip().split("\n")
    except FileNotFoundError:
        print(f"Error: file '{file_path}' not found")
    except Exception as e:
        print(f"Error: {e}")
    return None


def extract_data(lines: list[str]) -> list:
    question_answers, answers = [], []

    for line in lines:
        if "True or False:" in line:
            question_answers.append(
                {"type": "true_false", "question": re.sub(r"^[0-9.]+ ", "", line)}
            )
        elif line[0].isdigit():
            answers = []
            if "Choose all that apply" in line:
                question_answers.append(
                    {
                        "type": "multiple_choice",
                        "question": re.sub(r"^[0-9.]+ ", "", line),
                        "answers": answers,
                    }
                )
            else:
                question_answers.append(
                    {
                        "type": "single_choice",
                        "question": re.sub(r"^[0-9.]+ ", "", line),
                        "answers": answers,
                    }
                )
        elif line[0].isalpha():
            answers.append(re.sub(r"^[a-zA-Z.]+ ", "", line))

    return question_answers


def main():
    print("Hello from Zoom Poll Builder!")

    data_list = open_file("zoom_poll_builder/questions.txt")

    questions_and_answers = extract_data(data_list)
    # print(questions_and_answers)

    for x in questions_and_answers:
        print(x)


if __name__ == "__main__":
    main()
