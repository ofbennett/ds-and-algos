TEST_DIR="./build/bin/";
if [ ! -d "$TEST_DIR" ]; then
    echo "ERROR:";
    echo "/build/bin/ does not exist. Therefore no tests were run.";
    echo "You probably haven't compiled the project's C++ code yet! See the repo README for instructions on how to do that.";
    exit;
fi

echo "Collection test binaries...";
echo;

for f in build/bin/test_*; do
    echo "Running: $f";
    $f;
done
