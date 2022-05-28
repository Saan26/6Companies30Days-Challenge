# Capacity To Ship Packages Within D Days

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def getNeededDays(kilos):
            neededDays=1
            shipmentSize=0
            for package in weights:
                if shipmentSize+package<=kilos:
                    shipmentSize+=package
                else:
                    shipmentSize=package
                    neededDays+=1
            return neededDays
        
		
        def binarySearch(l,h):
            while l<h:
                kilos=(l+h)//2
                if getNeededDays(kilos)<=days:
                    h=kilos
                else:
                    l=kilos+1
            return l


        l=max(weights)
        h=sum(weights)
        return binarySearch(l,h)