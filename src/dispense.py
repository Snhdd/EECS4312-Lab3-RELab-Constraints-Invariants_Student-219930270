MAX_DAILY_DOSE = {
    "Aspirin": 4000,
    "Ibuprofen": 3200,
    "Paracetamol": 3000
}

class DispenseEvent:
    def __init__(self, patient_id, medication, dose_mg, quantity):

        if dose_mg <= 0:
            raise ValueError("Dose must be positive")

        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer")

        if medication not in MAX_DAILY_DOSE:
            raise ValueError("Unknown medication")

        if dose_mg > MAX_DAILY_DOSE[medication]:
            raise ValueError("Exceeds max daily dose")

        self.patient_id = patient_id
        self.medication = medication
        self.dose_mg = dose_mg
        self.quantity = quantity


def invariant_holds(existing_events, new_event):
    for event in existing_events:
        if event.patient_id == new_event.patient_id and event.medication == new_event.medication:
            return False
    return True

