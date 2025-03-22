import logging
import os

logging.basicConfig(level=logging.ERROR)


def generate_invitations(template, attendees):

    if not isinstance(template, str):
        logging.error('Template must be a string')
        return
    if not template:
        logging.error('Template is empty, no output files generated.')
        return

    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        logging.error('attendees must be a list of dict')
        return
    if not attendees:
        logging.error('No data provided, no output files generated.')
        return

    for index, attendee in enumerate(attendees, start=1):
        try:
            processed = template
            for key in ['name', 'event_title', 'event_date', 'event_location']:
                placeholder = "{" + key + "}"
                value = attendee.get(key, None)
                replacement = "N/A" if value is None else str(value)
                processed = processed.replace(placeholder, replacement)
            filename = f"output_{index}.txt"
            if os.path.exists(filename):
                print(f"Warning: {filename} already exists, overwriting it.")
            with open(filename, 'w') as f:
                f.write(processed)
            print(f"Invitation written to {filename}")
        except Exception as e:
            logging.error(f"Error processing attendee {index}: {str(e)}")
