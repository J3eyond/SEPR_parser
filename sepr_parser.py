from sys import argv
from bs4 import BeautifulSoup


def read_report(filename):
    with open(filename, "r") as f:
        content = f.read()
        return content


def parse_report(data):
    soup = BeautifulSoup(data, "lxml")
    blocked = [td.text for td in soup.find_all("tr", "blocked")]
    blocked = [del_special_chars(element) for element in blocked]
    quarantined = [td.text for td in soup.find_all("tr", "quarantined")]
    quarantined = [del_special_chars(element) for element in quarantined]
    deleted = [td.text for td in soup.find_all("tr", "deleted")]
    deleted = [del_special_chars(element) for element in deleted]
    new_infect = [td.text for td in soup.find_all("tr", "newly_infected")]
    new_infect = [del_special_chars(element) for element in new_infect]
    still_infected = [td.text for td in soup.find_all("tr", "still_infected")]
    still_infected = [del_special_chars(element) for element in still_infected]

    av_engine_off = [td.text for td in soup.find_all("tr", "av_by_type")]
    av_engine_off = [del_special_chars(element) for element in av_engine_off]
    sonar_pro_off = [td.text for td in soup.find_all("tr", "ptp_by_type")]
    sonar_pro_off = [del_special_chars(element) for element in sonar_pro_off]

    risk_category = [
        combine_every_three_elements(blocked),
        combine_every_three_elements(quarantined),
        combine_every_three_elements(deleted),
        combine_every_three_elements(new_infect),
        combine_every_three_elements(still_infected),
    ]

    risk_category_names = [
        "Blocked",
        "Quarantined",
        "Deleted",
        "Newly infected",
        "Still infected",
    ]

    av_status = [av_engine_off, sonar_pro_off]
    av_status_names = [
        "AV engine off",
        "Sonar pro scan off",
    ]

    return risk_category, risk_category_names, av_status, av_status_names


def combine_every_three_elements(old_list):
    return ["".join(x) for x in zip(old_list[0::3], old_list[1::3])]


def del_special_chars(string):
    return (
        string.replace("\n\xa0\n", " ")
        .replace("\n", " ")
        .replace("\xa0", " ")
        .replace("\t", " ")
    )


def output_to_files(*args):
    exception_string = "Filename: Unavailable"

    for category, filename in zip(args[0], args[1]):
        if len(category) > 0:
            print(f"\n {filename}: \n")
            with open(f"risk_category/{filename}.txt", "w") as file:
                for data in category:
                    if exception_string not in data:
                        file.write(str(data) + "\n")
                        print(data)

    for av_status, filename in zip(args[2], args[3]):
        if len(av_status) > 0:
            print(f"\n {filename}: \n")
            with open(f"av_status/{filename}.txt", "w") as file:
                for data in av_status:
                    file.write(str(data) + "\n")
                    print(data)


if __name__ == "__main__":
    if len(argv) < 2:
        print("[-] Example: python3 sep_report_parser.py report.html")
    else:
        risk, r_category, status, s_names = parse_report(read_report(argv[1]))
        output_to_files(risk, r_category, status, s_names)
