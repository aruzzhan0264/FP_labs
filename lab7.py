#  lab 7: var 6.

from typing import List


#   Мәтіндік файлдан деректерді оқу функциясы
def read_data_from_file(filename: str) -> List[str]:
    with open(filename, 'r') as file:
        return file.readlines()


#   Деректерді өңдеу функциясы
def process_data(data: List[str]) -> List[str]:
    processed_data = []
    for line in data:
        # егер жолда қос нүкте болса, жолды қос нүкте бойынша 2-ге бөлеміз
        parts = line.split(":")
        if len(parts) > 1:
            # алғашқы сөздің 1-ші әріпін кіші әріптен бас әріпке ауыстырамыз
            processed_line = parts[0].strip().capitalize() + ":" + ":".join(parts[1:]).strip()
        else:
            # егер жолда қос нүкте болмаса, қосымша бос орындарды алып тастаймыз
            processed_line = line.strip()
        processed_data.append(processed_line)

        # бос жолы болса оны жоямыз
        if not processed_data[-1]:
            processed_data.pop()

    # Жаңа жолдарды қосымша бос орындарсыз қосып, оларды соңғы өңделген жолға қосамыз
    processed_data[-1] += '\nHard skills: Python, C++, Java, HTML, CSS, PostgreSQL, Django'
    processed_data.append('Design skills: Figma, Adobe Photoshop, Adobe Illustrator, Adobe After Effects')
    processed_data.append('Soft skills: communicative, responsible, insightful')

    return processed_data


#    Өңделген деректерді файлға жазу функциясы

def write_data_to_file(filename: str, processed_data: List[str]) -> None:
    with open(filename, 'w') as file:
        file.write("\n".join(processed_data))


#   Деректерді өңдеудің барлық қадамдарын біріктіретін негізгі функция
def main(input_text: str, output_text: str) -> None:
    data = read_data_from_file(input_text)
    processed_data = process_data(data)
    write_data_to_file(output_text, processed_data)


#   қолдану мысалы
if __name__ == "__main__":
    input_filename = "../aruu.txt"
    output_filename = "../Aruzhan.txt"
    main(input_filename, output_filename)
