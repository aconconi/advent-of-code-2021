"""
    Advent of Code 2021
    Day 16: Packet Decoder
"""

from math import prod


def parse_input(file_name):
    with open(file_name, "r", encoding="ascii") as data_file:
        return data_file.readline()


def hex_to_bits(hexdata):
    return "".join(format(byte, "08b") for byte in bytes.fromhex(hexdata))


class BitsTransmission:
    def __init__(self, bits):
        self.bits = bits
        self.pos = 0

    def read_bits(self, n):
        ans = self.bits[self.pos : self.pos + n]
        self.pos += n
        return ans

    def read_int(self, n):
        return int(self.read_bits(n), 2)


class PacketParser:
    def __init__(self, bits):
        self.version = bits.read_int(3)
        self.typeID = bits.read_int(3)
        self.payload = self.read_payload(bits, self.typeID)

    @staticmethod
    def read_payload(bits, typeID):
        # Packets with type ID 4 represent a literal value.
        if typeID == 4:
            return PacketParser.read_literal(bits)

        # Every other type of packet (any packet with a
        # type ID other than 4) represent an operator.
        #
        # If the length type ID is 1, then the next 11 bits
        # are a number that represents the number of sub-packets
        # immediately contained by this packet.
        if bits.read_bits(1) == "1":
            return [PacketParser(bits) for _ in range(bits.read_int(11))]

        # If the length type ID is 0, then the next 15 bits are a number
        # that represents the total length in bits of the sub-packets
        # contained by this packet.
        size = bits.read_int(15)
        return PacketParser.read_subpackets_by_len(bits, size)

    @staticmethod
    def read_literal(bits):
        literal = ""
        while chunk := bits.read_bits(5):
            literal += chunk[1:]
            if chunk[0] == "0":
                break
        return int(literal, 2)

    @staticmethod
    def read_subpackets_by_len(bits, size):
        end_pos = bits.pos + size
        packets = []
        while bits.pos < end_pos:
            packets.append(PacketParser(bits))
        return packets

    def sum_versions(self):
        return (
            self.version
            if self.typeID == 4
            else self.version + sum(p.sum_versions() for p in self.payload)
        )

    def evaluate(self):
        func = {
            0: sum,
            1: prod,
            2: min,
            3: max,
            4: lambda x: x[0],
            5: lambda x: x[0] > x[1],
            6: lambda x: x[0] < x[1],
            7: lambda x: x[0] == x[1]
        }
        return func[self.typeID](
            [self.payload] if self.typeID == 4 else [p.evaluate() for p in self.payload]
        )


def day16_part1(data):
    return PacketParser(BitsTransmission(hex_to_bits(data))).sum_versions()


def day16_part2(data):
    return PacketParser(BitsTransmission(hex_to_bits(data))).evaluate()


def test_day16_part1():
    assert day16_part1("8A004A801A8002F478") == 16
    assert day16_part1("620080001611562C8802118E34") == 12
    assert day16_part1("C0015000016115A2E0802F182340") == 23
    assert day16_part1("A0016C880162017C3686B18A3D4780") == 31


def test_day16_part2():
    assert day16_part2("C200B40A82") == 3
    assert day16_part2("04005AC33890") == 54
    assert day16_part2("880086C3E88112") == 7
    assert day16_part2("CE00C43D881120") == 9
    assert day16_part2("D8005AC2A8F0") == 1
    assert day16_part2("F600BC2D8F") == 0
    assert day16_part2("9C005AC2F8F0") == 0
    assert day16_part2("9C0141080250320F1802104A08") == 1


if __name__ == "__main__":
    input_data = parse_input("data/day16.txt")

    print("Day 16 Part 1:")
    print(day16_part1(input_data))  # Correct answer is 1038

    print("Day 16 Part 2:")
    print(day16_part2(input_data))  # Correct answer is 246761930504
