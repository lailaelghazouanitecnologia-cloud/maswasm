"""
Function: $func84
Name: deblock_filter
Category: webp
Depth: 0
Status: done

Calls: none
Called by: 4 functions ($func1064, $func1005, $func1062, $func1003)

Deblocking filter for WebP/VP8 decoder.
Applies edge filtering to reduce blocking artifacts.

This is a loop filter that processes block edges, comparing pixel
differences against thresholds and applying smoothing when needed.

Global addresses:
- 16076: filter parameter 1
- 16308: filter parameter 2
- 17088: lookup table 1
- 17616: lookup table 2

Args:
    $var0: pixel buffer pointer
    $var1: stride (row width)
    $var2: stride increment
    $var3: number of iterations (height)
    $var4: threshold parameter 1
    $var5: threshold parameter 2
    $var6: filter strength
"""

from tzar._runtime import i32_load, i32_load8_u, i32_store8


def deblock_filter(
    buffer_ptr: int,
    stride: int,
    stride_inc: int,
    iterations: int,
    threshold1: int,
    threshold2: int,
    strength: int
) -> None:
    """
    Apply deblocking filter to image/video data.

    Processes vertical or horizontal edges depending on stride parameters.
    Uses lookup tables for edge decisions and filter values.

    Args:
        buffer_ptr: Pointer to pixel buffer
        stride: Row stride in bytes
        stride_inc: Increment between processed rows
        iterations: Number of rows/columns to process
        threshold1: Edge detection threshold
        threshold2: Secondary threshold
        strength: Filter strength parameter
    """
    if iterations <= 0:
        return

    # Calculate stride offsets
    stride_x2 = stride * 2
    stride_x3 = stride * 3
    stride_x4 = stride * 4
    neg_stride = -stride
    neg_stride_x2 = -stride_x2
    neg_stride_x3 = -stride_x3
    neg_stride_x4 = -stride_x4

    # Threshold calculation
    threshold_combined = (threshold1 << 1) | 1

    # Load filter lookup tables
    table1 = i32_load(16076)
    table2 = i32_load(17088)
    table3 = i32_load(16308)
    table4 = i32_load(17616)

    ptr = buffer_ptr
    count = iterations

    while count > 0:
        # Get pixels around the edge
        p2 = i32_load8_u(ptr + neg_stride_x2)  # p[-2]
        p1 = i32_load8_u(ptr + neg_stride)     # p[-1]
        p0 = i32_load8_u(ptr)                   # p[0]
        q0 = i32_load8_u(ptr + stride)         # p[1]
        q1 = i32_load8_u(ptr + stride_x2)      # p[2]
        q2 = i32_load8_u(ptr + stride_x3)      # p[3]

        # Edge detection using lookup tables
        diff1 = p1 - q0
        diff2 = p0 - p1

        edge_val1 = i32_load8_u(table4 + diff1)
        edge_val2 = i32_load8_u(table4 + diff2)

        # Combined edge check
        if (edge_val1 + edge_val2 * 4) <= threshold_combined:
            # More edge checks
            p3 = i32_load8_u(ptr + neg_stride_x4)
            q3 = i32_load8_u(ptr + stride_x4)

            diff3 = p3 - p2
            diff4 = p2 - p1
            diff5 = q1 - q0

            # Apply filter if all thresholds pass
            if (i32_load8_u(table4 + diff3) <= threshold2 and
                i32_load8_u(table4 + diff4) <= threshold2 and
                i32_load8_u(table4 + diff5) <= threshold2):

                # Calculate filter values
                filter_val = i32_load8_u(table3 + diff1)

                # Apply filtered values
                new_p0 = i32_load8_u(table2 + p0 + filter_val)
                new_q0 = i32_load8_u(table2 + q0 - filter_val)

                i32_store8(ptr, new_p0)
                i32_store8(ptr + stride, new_q0)

        # Move to next row/column
        ptr += stride_inc
        count -= 1


# Alias for WASM function name
func84 = deblock_filter
