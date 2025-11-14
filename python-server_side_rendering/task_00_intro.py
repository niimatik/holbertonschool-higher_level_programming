#!usr/bin/python3

def generate_invitations(template, attendees):
    invalide_template = not isinstance(template, str)
    invalide_list = not isinstance(attendees, list)
    invalide_element = not all(isinstance(attendee, dict)
                               for attendee in attendees)

    if invalide_list or invalide_template or invalide_element:
        print("invalide type")
        return

    if template.strip() == "":
        print("template empty")
        return

    if not attendees:
        print("no data provide")
        return

    for index, attendees in enumerate(attendees, start=1):
        invite = template

        name = attendees.get("name") or "N/A"
        invite = invite.replace("{name}", name)

        event_title = attendees.get("event_title") or "N/A"
        invite = invite.replace("{event_title}", event_title)

        event_date = attendees.get("event_date") or "N/A"
        invite = invite.replace("{event_date}", event_date)

        event_location = attendees.get("event_location") or "N/A"
        invite = invite.replace("{event_location}", event_location)

        filename = f"output_{index}.txt"
        with open(filename, "w") as file:
            file.write(invite)
