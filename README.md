# PokeAD
Active Directory project using PokeAPI to generate AD source object and populate AD server.

## Overview ##

Setting up an Azure Actice Directory and DHCP servers that combine:

1. A python program (or PS script) that makes a call  to the Pokémon API, retrieves the require information for the AD objects and writes it into the AD source object file (CSV or JSON).
    - Source Object File Schema:
        - Pokémon Number → Unique Identifier
        - Pokémon Name → Username
        - Pokémon Type → OU lvl 2
        - Pokémon Region → OU lvl 1
     
2. A PS script that automates the creation of the AD source object file based on a specified schedule.
    - AD server will start with Kanto OU as test/base.
    - First upload test (Johto) will be 10mins
    - Second upload test (Hoenn) will be 1hr
    - Third upload test (Sinnoh) will be 1day
    - Fourth upload test (Unova / Kalos) will be 1day
    - Sixth upload test ( Alola / Galar / Paldea)

3. DHCP server assignment based on region  + pokemon number
    - DHCP rules to consider total # of Pokemon per region when creating IP Range.
    - Kanto: 192.169.001.130 → Gyarados
