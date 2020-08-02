from opentrons import protocol_api

# metadata
metadata = {
    'protocolName': 'Golden Gate Hard Coded',
    'author': 'Benedict Carling',
    'description': 'Hard Coded exploration into Golden Gate assembly',
    'apiLevel': '2.2'
}

# protocol run function. the part after the colon lets your editor know
# where to look for autocomplete suggestions
def run(protocol: protocol_api.ProtocolContext):

    # labware
    my_thermocycler = protocol.load_module('thermocycler')
    thermo_plate = my_thermocycler.load_labware('nest_96_wellplate_100ul_pcr_full_skirt')
    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', '2')

    # pipettes
    left_pipette = protocol.load_instrument(
         'p300_single', 'left', tip_racks=[tiprack])

    # commands
    my_thermocycler.open_lid()

    # command 1 mix all liquids into A2
    left_pipette.pick_up_tip()
    left_pipette.aspirate(1, thermo_plate['A1'])
    left_pipette.dispense(1, thermo_plate['A2'])
    left_pipette.drop_tip()
    left_pipette.pick_up_tip()
    left_pipette.aspirate(18, thermo_plate['B1'])
    left_pipette.dispense(18, thermo_plate['A2'])
    left_pipette.drop_tip()
    left_pipette.pick_up_tip()
    left_pipette.aspirate(2.5, thermo_plate['C1'])
    left_pipette.dispense(2.5, thermo_plate['A2'])
    left_pipette.drop_tip()
    left_pipette.pick_up_tip()
    left_pipette.aspirate(0.5, thermo_plate['D1'])
    left_pipette.dispense(0.5, thermo_plate['A2'])
    left_pipette.drop_tip()
    left_pipette.pick_up_tip()
    left_pipette.aspirate(1.5, thermo_plate['E1'])
    left_pipette.dispense(0.5, thermo_plate['A2'])
    left_pipette.drop_tip()
    left_pipette.pick_up_tip()
    left_pipette.aspirate(1.5, thermo_plate['F1'])
    left_pipette.dispense(0.5, thermo_plate['A2'])

    # command 2 mix
    left_pipette.mix(repetitions=4,volume=25)
    left_pipette.drop_tip()

    # command 3 pause for 1 second in centrifuge
    # uncomment when working with real machine, when simmulate we autocontinue
    protocol.pause("Centrifuge well A2 for 1 second.")
    protocol.resume()

    # command 4 heat profile
    my_thermocycler.close_lid()
    my_thermocycler.set_lid_temperature(37)

    profile = [
        {'temperature': 37, 'hold_time_seconds': 300},
        {'temperature': 16, 'hold_time_seconds': 300}]
    
    my_thermocycler.execute_profile(steps=profile, repetitions=30, block_max_volume=30)
    my_thermocycler.set_block_temperature(60,300)