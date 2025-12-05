from amadeus import Client, ResponseError

# Replace with your keys
amadeus = Client(
    client_id='hgsv4BpSRgzhV2zpMfHOvGLroPwGhpZ6',
    client_secret='4zWQ6imwYAGAVDYN'
)

try:
    # Example: Riyadh (RUH) -> Abha (AHB) on Sept 20, 2025
    response = amadeus.shopping.flight_offers_search.get(
        originLocationCode='RUH',
        destinationLocationCode='AHB',
        departureDate='2025-09-20',
        adults=1,        
        children=0,
        currencyCode='SAR'
    )
    offers = response.data
 
 # Just show the first 5 offers in clean format
    for offer in offers[:5]:
        price = offer['price']['total']
        currency = offer['price']['currency']
        segments = offer['itineraries'][0]['segments']
        first_segment = segments[0]
        dep = first_segment['departure']['at']
        arr = first_segment['arrival']['at']
        airline = first_segment['carrierCode']

    print(f"{airline}: {price} {currency} | {dep} → {arr}")

except ResponseError as error:
    print(error)
