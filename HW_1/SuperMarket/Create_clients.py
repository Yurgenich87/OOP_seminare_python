from HW_1.SuperMarket.Classes.Clients import Market, OrdinaryClient, SpecialClient, TaxService

if __name__ == '__main__':
    market = Market()
    item1 = OrdinaryClient("Boris")
    item2 = SpecialClient("Fedor")
    item3 = OrdinaryClient("Dasha")
    item4 = TaxService()

    market.acceptToMarket(item1)
    market.acceptToMarket(item2)
    market.acceptToMarket(item3)
    market.acceptToMarket(item4)
    market.update()
