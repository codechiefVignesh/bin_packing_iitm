#ifndef THREEPHASE_TWO
#define THREEPHASE_TWO

#include <vector>
#include <boost/serialization/nvp.hpp>
#include <boost/archive/xml_oarchive.hpp>
#include <algorithm>
#include <climits>

using namespace std;

class Cuboid 
{
    protected:
        vector<vector<int>> corners;

    public:
        template<class Archive>
        void serialize(Archive &ar, const unsigned int file_version)
        {
            ar & boost::serialization::make_nvp("width", width);
            ar & boost::serialization::make_nvp("height", height);
            ar & boost::serialization::make_nvp("depth", depth);
            ar & boost::serialization::make_nvp("x", x);
            ar & boost::serialization::make_nvp("y", y);
            ar & boost::serialization::make_nvp("z", z);
        }

        Cuboid() : width(0), height(0), depth(0), x(0), y(0), z(0) {}

        Cuboid(float w, float h, float d, float x, float y, float z) :
            width(w), height(h), depth(d), x(x), y(y), z(z) {}

        float width;
        float height;
        float depth;
        float x;
        float y;
        float z;
        bool isPlaced = false;

        vector<vector<int>> compute_corners(const vector<vector<int>>& I, int W, int H)
        {
            corners.clear();

            if (I.empty())
            {
                corners.push_back({0, 0});
                return corners;
            }

            // Phase 1: Identify extreme boxes
            int x = 0;
            int m = 0;
            vector<int> e(I.size(), -1);

            for (size_t j = 0; j < I.size(); ++j)
            {
                if (x + I[j][0] > x)
                {
                    m++;
                    e[m - 1] = j;
                    x = x + I[j][0];
                }
            }

            // Phase 2: Determine the corner points
            corners.push_back({0, I[e[0]][1]});
            for (int j = 1; j < m; ++j)
            {
                corners.push_back({I[e[j - 1]][0], I[e[j]][1]});
            }
            corners.push_back({I[e[m - 1]][0], 0});

            // Phase 3: Remove infeasible corner points
            for (size_t i = 0; i < corners.size(); ++i)
            {
                int minWidth = INT_MAX;
                int minHeight = INT_MAX;

                for (const auto& box : I)
                {
                    minWidth = min(minWidth, box[0]);
                    minHeight = min(minHeight, box[1]);
                }

                if (corners[i][0] + minWidth > W || corners[i][1] + minHeight > H)
                {
                    corners.erase(corners.begin() + i);
                    --i; // Adjust index due to erase
                }
            }

            return corners;
        }
};

#endif
