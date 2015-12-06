/*
 * Codeforces Educational Round #2
 *
 * Problem 600 D. Area of Two Circles' Intersection
 *
 * author: yamaton
 * date: 2015-11-30
 *
 */

#include <cmath>
#include <cstdio>
#include <iostream>
#include <iomanip>

using namespace std;
typedef long double ld;

const ld pi = acos(-1);


ld solve(ld r1, ld r2, ld d) {
    if (d >= r1 + r2) {
        return 0.0;
    }
    if (max(r1, r2) >= min(r1, r2) + d) {
        auto tmp = min(r1, r2);
        return pi * tmp * tmp;
    }

    const ld r1sq = r1 * r1;
    const ld r2sq = r2 * r2;
    const ld dsq = d * d;

    const ld theta1 = acos(((r1 + r2) * (r1 - r2) + dsq) / (2. * d * r1));
    const ld theta2 = acos(((r2 + r1) * (r2 - r1) + dsq) / (2. * d * r2));
    // ld circsec1 = r1sq * theta1;
    // ld circsec2 = r2sq * theta2;
    // ld kite = r2 * d * sin(theta2);

    const ld area1 = r1sq * (theta1 - 0.5 * sin(2 * theta1));
    const ld area2 = r2sq * (theta2 - 0.5 * sin(2 * theta2));

    // cout << "circsec1: " << circsec1 << endl;
    // cout << "circsec2: " << circsec2 << endl;
    // cout << "kite    : " << kite << endl;

    // return circsec1 + circsec2 - kite;
    return area1 + area2;
}


int main() {
    ld x1, y1, r1;
    cin >> x1 >> y1 >> r1;
    ld x2, y2, r2;
    cin >> x2 >> y2 >> r2;

    ld d = hypot(x1 - x2, y1 - y2);
    auto res = solve(r1, r2, d);
    cout << setprecision(21) << res << endl;

    // codeforces gets crazy with this; WHY???
    // printf("%.20Lf\n", res);
}
