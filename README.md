# Final Report

## Team Members

Bradley Lewis, Alex Shi, and Joseph Zhang

## Description

We built a new tool on top of the *Flash Fast Network Verification* algorithm that employs a router parser, rule builder, and path constructor to quickly build all fastest paths for source-destination IP pairs of interest. This tool can be used to speedily verify networks, identify commonly used links, and visualize packets as they move through devices.

## Source Code

https://github.com/BradleyLewis08/flash-final/tree/mininet

## Production Efforts

### Code Walkthrough

**FIBs**: Our functionality would be incomplete without working with FIBs, so converting from generic formats to our intermediate representation of the flash format was our first priority.
1. We built a custom network 'customNetwork.py' that would interface with miniNet, an open source software that imitates fully set up systems, to create a realistic dummy network for our simulation.
2. We built a function 'mininetParser.py' that takes the bare bones routing information that miniNet gives us along with the network topology information and constructs FIBs in JUNOS format through our custom routing protocol.

**FLASH**: To build on flash, we created functionalities in five key areas.

1. New `GenericLoader` class that can take in any network and topology to run flash in one go. Ideally, we want to modify this in the future to run on a thread so that it can be repeatedly executed with updates.
2. New `Pairs` class that helps quickly map all common destinations to their respective sources, as well as all source-destination pairs with their paths. Provides a clean interface to get and iterate through IP pair information.
3. New `BDDEngine` functions used to:
    1. Map an arbitrary destination to its closest match predicate
    2. Use intersection to find the best union predicate in the equivalence class
4. New `InverseModel` function to iterate through pairs based on common predicate matches in destination and perform directed graph traversal to construct paths.
5. New `OutputManager` class that handles dumping formatted source-destination IP pairs and their paths into `csv` or `sql`.

The general process through which we run the flash algorithm is as follows:

1. Load network and topology into `GenericLoader` and create the `Pairs` object
2. Create an inverse model with flash
3. Verify the inverse model and update it with the new batch of rules
4. Construct path from generated equivalence classes
    1. Iterate through each destination
    2. Match with a predicate
    3. Use one ruleset to perform simplified graph traversal for all source packets based on starting port and device
    4. Add to `Pairs`
5. Dump newly calculated paths into `csv` or `sql`

### Methods for evaluation

We evaluated using a simulated *mininet* network, as well as the I2 (Internet 2) network. We find that with our network simulator, parser, and algorithm, we could efficiently reconstruct correct fastest paths for all of our source destination pairs, matching them with the FIB table forwarding rules. On the I2 network, our algorithm runs in under 1.5 seconds.

## Future work

We hope to use this algorithm for several more future use cases.

1. Creating a front end that allows large networks to interface with the tool, visualizing paths on actual devices and simulating counterfactuals with their networks.
2. Adding support for inverse functionality, namely mapping links to all source destination pairs that will take them, thus giving admins visibility on network usage.
3. 

Additionally, some improvements we would like to make are:

1. Caching optimizations on our Flash implementation to improve our asymptotic run time.
