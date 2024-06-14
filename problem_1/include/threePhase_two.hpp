#ifndef THREEPHASE_TWO
#define THREEPHASE_TWO


#include <vector>
#include <map>
#include <boost/serialization/nvp.hpp>
#include <boost/archive/xml_oarchive.hpp>

using namespace std;

class Cuboid 
{
    protected:
        vector<vector<int>> corners;
    public:
        Cuboid() {}
        Cuboid(int w, int h) :
            width(w), height(h){}

        template<class Archive>
        void serialize(Archive &ar, const unsigned int file_verision)
        {
            ar & boost::serialization::make_nvp("width", width);
            ar & boost::serialization::make_nvp("height", height);
            // ar & boost::serialization::make_nvp("depth", depth);
            ar & boost::serialization::make_nvp("x", x);
            ar & boost::serialization::make_nvp("y", y);
            // ar & boost::serialization::make_nvp("z", z);
        }

        float width;
        float height;
        // float depth;
        float x = 0;
        float y = 0;
        // float z = 0;
        bool isPlaced = false;
    
        vector<vector<int>> compute_corners(map<string , vector<vector<int>>> &I)
        {   
            if(I.size()==0)
            {
                this->corners.push_back({0,0});
                return this->corners;
            }
            //phase - 1
            int x = 0;
            int m = 0;
            for(int j = 0; j<I.size(); j++)
            {
                if(I)
            }
        }



};

#endif