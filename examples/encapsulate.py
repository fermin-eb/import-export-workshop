
class OrderEncapsulated():
    def __init__(self, lineItems, country, state, city):
        self.lineItems = lineItems
        self.country = country
        self.state = state
        self.city = city

    def getOrderTotal(self):
        total = 0
        for item in self.lineItems:
            subtotal = item.price * item.quantity
            total += subtotal * self.getTaxRate()
        return total

    def getTaxRate(self):
        if country == 'US':
            return self.getUSTax(self.state)
        
        if country == 'EU':
            return self.getEUTax(self.country, self.product)

        if country == 'CN':
            return self.getCNTax(self.product)

    def getUSTax(self, state):
        pass

    def getEUTax(self, state):
        pass

    def getCNTax(self, state):
        pass

'''
Order delega todo lo relacionado con las TAXs
No tiene porque conocer como se calculan las tasas
'''
class OrderLessEncapsulate():
    def __init__(self, lineItems, country, state, city):
        self.lineItems = lineItems
        self.country = country
        self.state = state
        self.city = city
        self.taxCalculator = TaxCalculator() 
    
    def getOrderTotal(self):
        total = 0
        for item in self.lineItems:
            subtotal = item.price * item.quantity
            total += subtotal * taxCalculator.getRate(self.country, self.state, item.product)
        return total

class TaxCalculator():
    def getTaxRate(self, country, state, product):
        if country == 'US':
            return self.getUSTax(state)
        
        if country == 'EU':
            return self.getEUTax(country, product)

        if country == 'CN':
            return self.getCNTax(product)
        
        raise NotImplementedError("Country not implemented")

    def getUSTax(self, state):
        pass

    def getEUTax(self, country, product):
        pass

    def getCNTax(self, product):
        pass

'''
TaxCalculator() esta acoplado a OrderLessEncapsulated
-  Inversión de dependencias
Tell don't ask <- We should not ask object about their state, thell them what to do
'''
class Order():
    def __init__(self, lineItems, country, state, city, taxCalculator=None):
        self.lineItems = lineItems
        self.country = country
        self.state = state
        self.city = city

        if taxCalculator is None:
            taxCalculator = TaxCalculator()
        self.taxCalculator = taxCalculator
    
    def getOrderTotal(self):
        pass

class TaxCalculatorCajaB():
    def getTaxRate(self, country, state, product):
        return 0
order = Order([], 'ES', 'Alicante', 'Alicante', TaxCalculatorCajaB())

'''
If else if else if else == code smell
chain of responsibility
'''
class TaxCalculator():
    def __init__(self):
        self.calculatorByCountry = {
            'US': USTaxCalculator,
            'EU': EUTaxCalculator,
            'CN': CNTaxCalculator,
        }
    def getTaxRate(self, country, state, product):
        calculator = self.calculatorByCountry.get(country)
        if calculator is None:
            raise NotImplementedError("Country not implemented")

        return calculator(country, state, product)
        
def USTaxCalculator(country, state, product):
    pass

def EUTaxCalculator(country, state, product):
    pass        

def CNTaxCalculator(country, state, product):
    pass
