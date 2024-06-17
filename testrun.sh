cd ../

date=$(date +%Y-%m-%d)
resultDir="results-$date"

cd gas-benchmarks
./run.sh \
  -t "tests/" \
  -w "warmup/warmup-1000bl-16wi-24tx.txt" \
  -c "nethermind,reth,besu" \
  -r 1 \
  -o $resultDir
cp $resultDir/reports/index.html ../gas-data-demo/gas/$date.html
cp $resultDir/reports/result.json ../gas-data-demo/gas/$date.json

cd ../genesis-init-benchmarks
./runSpeed.sh \
  -t "tests/" \
  -c "nethermind,reth,besu" \
  -r 1 \
  -o "$resultDir/speed" \
  -s 1,2,10,100
cp $resultDir/speed/reports/speed.html ../gas-data-demo/genesis-init-memory/$date.html
cp $resultDir/speed/reports/speed.json ../gas-data-demo/genesis-init-memory/$date.json

./runMemory.sh \
  -t "tests/" \
  -c "nethermind,reth,besu" \
  -r 1 \
  -o "$resultDir/memory" \
  -s 1,2,10,100
cp $resultDir/memory/reports/memory.html ../gas-data-demo/genesis-init-memory/$date.html
cp $resultDir/memory/reports/memory.json ../gas-data-demo/genesis-init-memory/$date.json

cd ../burntpix-benchmarks
./run.sh \
  -t "testburnt/" \
  -w "./testburntwarm/warm.txt" \
  -c "nethermind,reth,besu" \
  -r 1 \
  -o $resultDir
cp $resultDir/reports/index.html ../gas-data-demo/burntpix/$date.html
cp $resultDir/reports/result.json ../gas-data-demo/burntpix/$date.json

cd ../gas-data-demo
./push.sh