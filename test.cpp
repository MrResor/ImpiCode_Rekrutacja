#include <iostream>
#include <set>
#include <limits>
#include <iomanip>

class Elephant 
{
    private:
        float *weights;
        int  *curr_order, *desr_order, el_count;
        std::set<std::set<int>> sets;

        // reads data from input buffer
        void read_data() 
        {
            std::cin >> el_count;
            int tmp;
            weights = new float[el_count];
            for (int i = 0; i < el_count; ++i)
                std::cin >> weights[i];
            curr_order = new int[el_count];
            for (int i = 0; i < el_count; ++i)
            {
                scanf("%d", &tmp);
                curr_order[i] = tmp - 1;
            }
            desr_order = new int[el_count];
            for (int i = 0; i < el_count; ++i)
            {
                scanf("%d", &tmp);
                desr_order[i] = tmp - 1;
            }
        } 
        // finds sets in the provided data
        void get_sets()
        {
            int *p = new int[el_count];
            bool *visited = new bool[el_count] {false};
            for (int i = 0; i < el_count; ++i)
                for (int j = 0; j < el_count; ++j)
                    if (desr_order[j] == i)
                    {
                        p[i] = curr_order[j];
                        break;
                    }
            int x;
            for (int i = 0; i < el_count; ++i)
            {
                if (!visited[i])
                {
                    std::set<int> tmp;
                    x = i;
                    while(!visited[x])
                    {
                        visited[x] = true;
                        tmp.insert(x);
                        x = p[x];
                    }
                    sets.insert(tmp);
                }
            }
        }
        // calculate result
        void algorithm()
        {   
            float glob_min = std::numeric_limits<float>::infinity();
            for (auto set: sets)
                for (auto s: set)
                    glob_min = std::min(weights[s], glob_min);
            long double res = 0;
            float sum, min;
            int len;
            for (auto set: sets)
            {
                sum = 0;
                len = 0;
                min = std::numeric_limits<float>::infinity();
                for (auto s: set)
                {
                    len += 1;
                    sum += weights[s];
                    min = std::min(min, weights[s]);
                }
                res += std::min(sum + (len - 2) * min, sum + min + (len + 1) * glob_min);
            }
            std::cout << std::setprecision(30) << res;
        }
        
    public:
        Elephant() {
            read_data();
            get_sets();
            algorithm();
        };

};

void main() 
{
    Elephant();
}