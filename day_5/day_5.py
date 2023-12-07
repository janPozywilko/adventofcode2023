import typer

def loadData(file):
    with open(f"{file}", "r") as f:
        d = f.read().splitlines()
    return d

def mapSeed(seed,map):
    for row in map:
        conversion = 0
        destination_start, source_start, step = row.split(' ')
        if int(seed) >= int(source_start) and int(seed) <= (int(source_start) + int(step)):
            conversion = int(destination_start) - int(source_start)
            return int(seed) + conversion
    return int(seed)
    

def main():
    seeds = loadData(file='seeds.txt')[0].split(' ')
    seed_to_soil = loadData(file='seed-to-soil.txt')
    soil_to_fertilizer = loadData(file='soil-to-fertilizer.txt')
    fertilazer_to_water = loadData(file='fertilizer-to-water.txt')
    water_to_light = loadData(file='water-to-light.txt')
    light_to_temperature = loadData(file='light-to-temperature.txt')
    temperature_to_humidity = loadData(file='temperature-to-humidity.txt')
    humidity_to_location = loadData(file='humidity-to-location.txt')
    locations = []
    for seed in seeds:
        mapped_seed = mapSeed(seed,seed_to_soil)
        mapped_soil = mapSeed(mapped_seed,soil_to_fertilizer)
        mapped_fertilizer = mapSeed(mapped_soil,fertilazer_to_water)
        mapped_water = mapSeed(mapped_fertilizer,water_to_light)
        mapped_light = mapSeed(mapped_water,light_to_temperature)
        mapped_temperature = mapSeed(mapped_light,temperature_to_humidity)
        mapped_humidity = mapSeed(mapped_temperature,humidity_to_location)
        locations.append(mapped_humidity
                             )
    print(f"Final Locations: {min(locations)}")
    


if __name__ == "__main__":
    typer.run(main)