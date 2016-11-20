from dateconversion import *

class TrainStop:
    def __init__(self, train):        
        
        self.date = date_from_text(train["BETRIEBSTAG"])
        self.ID = train["FAHRT_BEZEICHNER"]
        self.operator_ID = train["BETREIBER_ID"]
        self.operator = train["BETREIBER_ABK"]
        self.operator_name = train["BETREIBER_NAME"]
        self.transport_type = train["PRODUKT_ID"]
        self.line_type = train["LINIEN_ID"]
        self.line_text = train["LINIEN_TEXT"]
        self.detour_ID = train["UMLAUF_ID"]
        self.vehicle_text = train["VERKEHRSMITTEL_TEXT"]
        self.is_extra = bool(train["ZUSATZFAHRT_TF"])
        self.is_cancelled = bool(train["FAELLT_AUS_TF"])
        self.bpuic = train["BPUIC"]
        self.stop_name = train["HALTESTELLEN_NAME"]
        self.arrival_time = datetime_from_text(train["ANKUNFTSZEIT"])
        self.arrival_predicted = datetime_from_text(train["AN_PROGNOSE"])
        self.arrival_predicted_status = train["AN_PROGNOSE_STATUS"]
        self.departure_time = datetime_from_text(train["ABFAHRTSZEIT"])
        self.departure_predicted = datetime_from_text(train["AB_PROGNOSE"])
        self.departure_predicted_status = train["AB_PROGNOSE_STATUS"]
        self.is_coming_through = bool(train["DURCHFAHRT_TF"])
    
    def __str__(self):
        s = ""
        s += self.date.isoformat() + " "
        s += print_time(self.arrival_time) + " "
        s += self.stop_name
        return s
    
    def arrival_delay(self):
        delay = self.arrival_predicted - self.arrival_time
        delay_minutes = delay.total_seconds() / 60
        if delay_minutes < -600:
            delay_minutes = 0
        return delay_minutes
    
    def departure_delay(self):
        delay = self.departure_predicted - self.departure_time
        delay_minutes = delay.total_seconds() / 60
        if delay_minutes < -600:
            delay_minutes = 0
        return delay_minutes

