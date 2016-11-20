class TrainStop:
    def __init__(self, 
                 date,
                 ID,
                 operator_ID,
                 operator,
                 operator_name,
                 transport_type,
                 line_type,
                 line_text,
                 detour_ID,
                 vehicle_text,
                 is_extra,
                 is_cancelled,
                 bpuic,
                 stop_name, 
                 arrival_time,
                 arrival_predicted,
                 arrival_predicted_status,
                 departure_time,
                 departure_predicted,
                 departure_predicted_status,
                 is_coming_through):
        
        self.date = date_from_text(date)
        self.ID = ID
        self.operator_ID = operator_ID
        self.operator = operator
        self.operator_name = operator_name
        self.transport_type = transport_type
        self.line_type = line_type
        self.line_text = line_text
        self.detour_ID = detour_ID
        self.vehicle_text = vehicle_text
        self.is_extra = bool(is_extra)
        self.is_cancelled = bool(is_cancelled)
        self.bpuic = bpuic
        self.stop_name = stop_name
        self.arrival_time = datetime_from_text(arrival_time)
        self.arrival_predicted = datetime_from_text(arrival_predicted)
        self.arrival_predicted_status = arrival_predicted_status
        self.departure_time = datetime_from_text(departure_time)
        self.departure_predicted = datetime_from_text(departure_predicted)
        self.departure_predicted_status = departure_predicted_status
        self.is_coming_through = is_coming_through
    
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

# create TrainStop object from json-like format
def create_train_stop(train):
    return TrainStop(train["BETRIEBSTAG"],
              train["FAHRT_BEZEICHNER"],
              train["BETREIBER_ID"],
              train["BETREIBER_ABK"],
              train["BETREIBER_NAME"],
              train["PRODUKT_ID"],
              train["LINIEN_ID"],
              train["LINIEN_TEXT"],
              train["UMLAUF_ID"],
              train["VERKEHRSMITTEL_TEXT"],
              train["ZUSATZFAHRT_TF"],
              train["FAELLT_AUS_TF"],
              train["BPUIC"],
              train["HALTESTELLEN_NAME"],
              train["ANKUNFTSZEIT"],
              train["AN_PROGNOSE"],
              train["AN_PROGNOSE_STATUS"],
              train["ABFAHRTSZEIT"],
              train["AB_PROGNOSE"],
              train["AB_PROGNOSE_STATUS"],
              train["DURCHFAHRT_TF"])

