def readcom(fname):
    teams = {}

    with open(fname, 'r') as file:
        lines = file.readlines()
        teams_line = lines[0].strip()
        team1, team2 = teams_line.split(' versus ')
        teams[team1] = 0
        teams[team2] = 0

        for line in lines[1:]:
            parts = line.strip().split(' ')
            team = parts[0]
            minutes, seconds = map(int, parts[3].split(':'))
            time_in_seconds = minutes * 60 + seconds
            teams[team] += 1

    return teams


def main():
    comfile = "commentary.txt"
    result = readcom(comfile)

    result = sorted(result.items(), key=lambda x: x[1], reverse=True)

    for team, score in result:
        print(f"{team} {score}")


if __name__ == "__main__":
    main()
