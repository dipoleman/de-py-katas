
def years_of_growth(
    initial_population,
    target_population,
    growth_rate,
    net_migration
):
    total_population = initial_population
    years = 0
    while total_population < target_population:
        total_population = (total_population * (growth_rate + 100)/100) + net_migration
        years += 1

    return years
