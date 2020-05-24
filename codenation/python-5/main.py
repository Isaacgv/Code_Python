from datetime import datetime, timezone


records = [
    {'source': '48-996355555', 'destination': '48-666666666', 'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097', 'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097', 'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788', 'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788', 'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099', 'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697', 'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099', 'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697', 'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097', 'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564627800, 'start': 1564626000}
]


def classify_by_phone_number(records):

    taxa_records = dict()
    day_seconds = 60 * 10
    night_seconds = 60 * 14

    for record in records:
        n_seconds_day = 0
        total = 0
        tax_d = 0.36

        time_start = datetime.utcfromtimestamp(record["start"])
        time_start = time_start.replace(tzinfo=timezone.utc).astimezone()

        time_end = datetime.utcfromtimestamp(record["end"])
        time_end = time_end.replace(tzinfo=timezone.utc).astimezone()

        hr_start = time_start.timetuple().tm_hour

        n_seconds = (time_end - time_start).total_seconds() // 60

        if hr_start >= 22 or hr_start < 6:

            if n_seconds > night_seconds:
                n_seconds_day = n_seconds - night_seconds

        else:

            if n_seconds <= day_seconds:
                n_seconds_day = n_seconds

        total = n_seconds_day * 0.09 + tax_d

        if record["source"] in taxa_records:
            taxa_records[record["source"]] += total
        else:
            taxa_records[record["source"]] = total

    taxa_records = sorted(taxa_records.items(),
                          key=lambda x: x[1], reverse=True)

    clients_tax = []

    for client, tax in taxa_records:
        clients_tax.append(dict(source=client, total=round(tax, 2)))

    return(clients_tax)
