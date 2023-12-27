class Malware:
    description = ""
    name = "unidentified malware"
    signature = "0000"

    def get_description(self):
        return self.description


class Virus(Malware):
    def __init__(self, virus_description, virus_name, virus_signature):
        self.description = virus_description
        self.name = virus_name
        self.signature = virus_signature

    def infect(self, target_system):
        print(f"Oh! I'll create many copies of myself on the {target_system} "
              f"due to my {self.signature} code")    
        

class Worm(Malware):
    def __init__(self, worm_description, worm_name, worm_signature):
        self.description = worm_description
        self.name = worm_name
        self.signature = worm_signature

    def infect(self, protocol):
        print(f"Oh! I'll spread in your network using {protocol} "
              f"due to my {self.signature} code")


class Trojan(Malware):
    def __init__(self, trojan_description, trojan_name, trojan_signature, bait_feature):
        self.description = trojan_description
        self.name = trojan_name
        self.signature = trojan_signature
        self.bait_feature = bait_feature
    
    def perform_bait_feature(self):
        print(f"You will install me, because I can let you {self.bait_feature}")



