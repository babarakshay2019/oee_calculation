def calculate_oee(production_logs):
    IDEAL_CYCLE_TIME = 5 * 60  # Ideal time to produce one part in seconds
    SHIFTS = 3  # Number of shifts
    SHIFT_HOURS = 8  # Hours per shift
    AVAILABLE_TIME = SHIFTS * SHIFT_HOURS * 60 * 60  # Convert shift hours to seconds

    if not isinstance(production_logs, list):
        production_logs = [production_logs]  # Ensure it's a list for uniform processing

    if not production_logs:
        return 0, 0, 0, 0  # Handle case where there are no production logs

    actual_output = len(production_logs)  # Number of products produced
    available_operating_time = actual_output * IDEAL_CYCLE_TIME  # Available operating time based on number of products * ideal cycle time
    unplanned_downtime = AVAILABLE_TIME - available_operating_time  # Unplanned downtime is total available time minus operating time

    good_products = sum(1 for log in production_logs if log.duration.total_seconds() == IDEAL_CYCLE_TIME)  # Products produced exactly on IDEAL_CYCLE_TIME seconds
    bad_products = actual_output - good_products  # Products produced with a different duration
    total_products = good_products + bad_products

    availability = ((AVAILABLE_TIME - unplanned_downtime) / AVAILABLE_TIME) * 100
    performance = ((IDEAL_CYCLE_TIME * actual_output) / available_operating_time) * 100
    quality = (good_products / total_products) * 100

    oee = availability * performance * quality

    return oee, availability, performance, quality
