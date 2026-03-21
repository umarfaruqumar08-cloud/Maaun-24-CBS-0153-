from datetime import datetime


class Patient:
    """
    This is a blueprint for creating a patient.
    Think of it like a form: every patient has name, age, symptoms, etc.
    """
    
    def __init__(self, name, age, symptoms):
        # __init__ runs automatically when we create a new patient
        self.name = name
        self.age = age
        self.symptoms = symptoms
        # Automatically record what time they arrived
        self.arrival_time = datetime.now()
        # Create a unique ID based on time (like P143022 for 14:30:22)
        self.id = f"P{datetime.now().strftime('%H%M%S')}"
    
    def get_wait_time(self):
        """
        This method calculates how long patient has been waiting.
        It's a "behavior" - something the patient can do.
        """
        return datetime.now() - self.arrival_time
    
    def __str__(self):
        # This controls how the patient looks when printed
        return f"{self.id}: {self.name} ({self.age} yrs)"


class ClinicQueue:
    """
    This manages the line of patients using FIFO (First In, First Out).
    Like a queue at the bank - first person to arrive is first to be served.
    """
    
    def __init__(self):
        # The underscore means "this is private, don't touch directly"
        self._queue = []  # Empty list to store patients
        self._served_patients = []  # Keep track of finished patients
    
    def enqueue(self, patient):
        """
        Add patient to the END of the line.
        'enqueue' means 'add to queue'.
        """
        self._queue.append(patient)
        print(f"Added {patient.name} to queue. Position: {len(self._queue)}")
    
    def dequeue(self):
        """
        Remove and return the FIRST patient (FIFO).
        'dequeue' means 'remove from queue'.
        """
        if not self.is_empty():
            patient = self._queue.pop(0)  # pop(0) removes FIRST item
            self._served_patients.append(patient)
            return patient
        return None
    
    def peek(self):
        """
        Look at the first patient without removing them.
        """
        if not self.is_empty():
            return self._queue[0]
        return None
    
    def is_empty(self):
        """Check if queue is empty."""
        return len(self._queue) == 0
    
    def size(self):
        """How many people are waiting."""
        return len(self._queue)
    
    def get_all_patients(self):
        """Get list of all waiting patients."""
        return self._queue.copy()
    
    def get_total_served(self):
        """How many patients have been served today."""
        return len(self._served_patients)
    
    def get_queue_positions(self):
        """
        Return patients with their position numbers (1, 2, 3, etc.)
        """
        positions = []
        for i, patient in enumerate(self._queue):
            positions.append((i + 1, patient))
        return positions