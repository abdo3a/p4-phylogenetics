from p4.supertreesupport import SuperTreeInputTrees

stit = SuperTreeInputTrees('balanced64.nex')
stit.writeInputTreesToFile = True
stit.outputFile = 'inputtrees.tre'
stit.noTaxaToRemove = 32 
stit.noOutputTrees = 20
stit.generateInputTrees()


