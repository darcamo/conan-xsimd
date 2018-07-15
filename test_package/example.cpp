#include <iostream>
#include <xsimd/xsimd.hpp>
#include <xsimd/types/xsimd_sse_double.hpp>

namespace xs = xsimd;

int main(int argc, char* argv[])
{
    xs::batch<double, 2> a(1.5, 2.5);
    xs::batch<double, 2> b(2.5, 3.5);
    auto mean = (a + b) / 2;
    std::cout << mean << std::endl;
    return 0;
}
