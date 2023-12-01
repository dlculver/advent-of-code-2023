const std = @import("std");

pub fn main() !void {
    const file = try std.fs.cwd().openFile("input.txt", .{}); // Open file.
    defer file.close(); // Close file when done.

    var bufReader = std.io.bufferedReader(file.reader()); // Create buffered reader.
    var inStream = bufReader.reader();

    var sum: u32 = 0;
    var buf: [1024]u8 = undefined;
    while (try inStream.readUntilDelimiterOrEof(&buf, '\n')) |line| {
        std.debug.print("line: {s}\n", .{line});
        var firstDigit: i8 = -1;
        var lastDigit: i8 = -1;

        // loop over chars in line
        for (line) |char| {
            if (char >= '1' and char <= '9') {
                // std.debug.print("char: {c}\n", .{char});
                if (firstDigit == -1) {
                    firstDigit = @as(i8, @intCast(char - '0'));
                }
                lastDigit = @as(i8, @intCast(char - '0'));
            }
        }
        // concatenate the first and last numbers into a single number
        const number: i8 = firstDigit * 10 + lastDigit;
        std.debug.print("number: {d}\n", .{number});

        sum += @as(u32, @intCast(number));
    }
    std.debug.print("sum: {d}\n", .{sum});
}
