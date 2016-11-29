# Magic: The Gathering SDK

This is an iterator based implementation for Magic: The Gathering SDK. It is a wrapper around the MTG API of [magicthegathering.io](http://magicthegathering.io/).


## Requirements
Only python3.5+ is supported.

## Installation

Using pip:

    pip install mtgsdki

## quick start

    In [1]: from mtgsdk import cards
    
    In [2]: cards.search(name='avacyn')
    Out[2]: <generator object search at 0x7f8761c01780>
    
    In [3]: next(cards.search(name='avacyn'))
    Out[3]: Card(name="Avacyn's Pilgrim", set='pFNM')

    In [4]: list(filter(lambda c: 'angel' in c.name.lower(), cards.search(name='avacyn')))
    Out[4]: 
    [Card(name='Avacyn, Angel of Hope', set='AVR'),
    Card(name='Avacyn, Guardian Angel', set='M15'),
    Card(name='Avacyn, Angel of Hope', set='V15'),
    Card(name='Archangel Avacyn', set='SOI')]

As you can see, you will get generators that yield Cards (or Sets). You can use them as all the other iterators in python.

Go Wild!

## Usage

Import (Card and Set will be most used)

    from mtgsdk import cards
    from mtgsdk import sets
    from mtgsdk import types
    
### Properties Per Class

#### Card

    artist
    border
    cmc
    color_identity
    colors
    flavor
    foreign_names
    hand
    id
    image_url
    layout
    legalities
    life
    loyalty
    mana_cost
    multiverseid
    name
    names
    number
    original_text
    original_type
    power
    printings
    rarity
    release_date
    reserved
    rulings
    set
    set_name
    source
    starter
    subtypes
    supertypes
    text
    timeshifted
    toughness
    type
    types
    variations
    watermark


#### Set

    block
    booster
    border
    code
    gatherer_code
    magic_cards_info_code
    mkm_id
    mkm_name
    name
    old_code
    online_only
    release_date
    type
    
### Find Card by Multiverse Id

    card = cards.from_id(386616)
    
### search for Cards

    found_cards = cards.search(set='ktk', subtypes='warrior,human')
    
### Get all cards (will page through all the data)

    all_cards = cards.search()
    
### Get all cards, but only a specific page of data

    found_cards = cards.search(page=5, pageSize=1000)
The iterators will automatically page through all pages if you don't specify a page. Be careful when you consume the whole iterator, as this can take a long while!
    
### Find a Set by code

    khans_of_tarkir = sets.from_code('ktk')
    
### Get all sets

    all_sets = sets.search()
    
### Filter sets via query parameters

    found_sets = sets.search(name='khans')
    
### Get all types

    all_types = types.types()
    
### Get all subtypes

    all_subtypes = types.subtypes()
    
### Get all supertypes

    all_supertypes = types.supertypes()
    
## Contributing

1. Fork it ( https://github.com/MrGreenTea/mtgsdk/fork )
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request
