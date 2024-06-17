#include <boost/archive/xml_iarchive.hpp>
#include <iostream>
#include <fstream>
#include <string>
#include "include/threePhase_two.hpp"


using namespace std;

vector<vector<int>> readCuboidsFromXML(const string& filename)
{
    vector<vector<int>> I;

    try
    {
        ifstream ifs(filename);
        if (!ifs.is_open())
        {
            throw runtime_error("Unable to open file.");
        }

        boost::archive::xml_iarchive ia(ifs);

        while (ifs.good())
        {
            Cuboid cuboid;
            ia >> BOOST_SERIALIZATION_NVP(cuboid);
            I.push_back({static_cast<int>(cuboid.width), static_cast<int>(cuboid.height)});
        }
    }
    catch (const exception& e)
    {
        cerr << "Error: " << e.what() << endl;
    }

    return I;
}

int main()
{

    string filename = "cuboid.xml"; // Path to your XML file
    vector<vector<int>> I = readCuboidsFromXML(filename);
    vector<vector<int>> corners;
    int W, H;
    cout<<"Enter the Height and Width of the palette/bin/container: "<<endl;
    cout<<"Width :";
    cin>>W;
    cout<<endl;
    cout<<"Height :";
    cin>>H;
    cout<<endl;
    cout<<"Computing corners ..."<<endl;

    Cuboid c;
    corners = c.compute_corners(I,W,H);
    // cout<<"welcome";
    for(int i = 0; i<corners.size(); i++)
    {
        cout<<"Corner "<<i+1<<" "<<corners[i][0]<<","<<corners[i][1]<<endl;
    }
    return 0;
}
